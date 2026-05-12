import fs from "node:fs";
import path from "node:path";

const root = process.argv[2] ? path.resolve(process.argv[2]) : path.resolve("course-mvp");
const outDir = process.argv[3] ? path.resolve(process.argv[3]) : path.join(root, "pdfs");

const page = { width: 612, height: 792, margin: 54 };
const fonts = {
  regular: "F1",
  bold: "F2",
  mono: "F3",
};

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === "pdfs" || entry.name === "node_modules") return [];
      return walk(full);
    }
    return entry.isFile() && entry.name.endsWith(".md") ? [full] : [];
  });
}

function titleFrom(file, content) {
  const heading = content.split(/\r?\n/).find((line) => line.startsWith("# "));
  if (heading) return heading.replace(/^#\s+/, "").trim();
  return path.basename(file, ".md").replace(/[-_]/g, " ");
}

function normaliseMarkdown(markdown) {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const output = [];
  let inFence = false;

  for (const raw of lines) {
    let line = raw.replace(/\t/g, "    ").trimEnd();
    if (line.startsWith("```")) {
      inFence = !inFence;
      continue;
    }
    if (inFence) {
      output.push({ text: line, size: 9, font: "mono", gap: 2 });
      continue;
    }
    if (!line.trim()) {
      output.push({ text: "", size: 10, font: "regular", gap: 7 });
      continue;
    }
    if (/^\|?\s*-{3,}/.test(line.replace(/\|/g, "").trim())) continue;
    if (/^\s*\|/.test(line)) {
      const cells = line
        .split("|")
        .map((cell) => cell.trim())
        .filter(Boolean);
      if (cells.length) output.push({ text: cells.join("  |  "), size: 9.5, font: "regular", gap: 3 });
      continue;
    }
    const heading = line.match(/^(#{1,6})\s+(.*)$/);
    if (heading) {
      const level = heading[1].length;
      output.push({
        text: stripInline(heading[2]),
        size: level === 1 ? 18 : level === 2 ? 14 : 12,
        font: "bold",
        gap: level === 1 ? 12 : 8,
      });
      continue;
    }
    line = line.replace(/^(\s*)[-*]\s+/, "$1• ");
    output.push({ text: stripInline(line), size: 10.5, font: "regular", gap: 4 });
  }
  return output;
}

function stripInline(text) {
  return text
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1");
}

function wrapText(text, size) {
  if (!text) return [""];
  const maxWidth = page.width - page.margin * 2;
  const avgChar = size * 0.52;
  const maxChars = Math.max(24, Math.floor(maxWidth / avgChar));
  const words = text.split(/\s+/);
  const lines = [];
  let current = "";

  for (const word of words) {
    if (!current) {
      current = word;
    } else if ((current + " " + word).length <= maxChars) {
      current += " " + word;
    } else {
      lines.push(current);
      current = word;
    }
  }
  if (current) lines.push(current);
  return lines;
}

function escapePdf(text) {
  return text
    .replace(/\\/g, "\\\\")
    .replace(/\(/g, "\\(")
    .replace(/\)/g, "\\)")
    .replace(/[^\x09\x0A\x0D\x20-\x7E]/g, (char) => {
      if (char === "•") return "\\267";
      return "";
    });
}

function makePages(blocks, docTitle) {
  const pages = [];
  let commands = [];
  let y = page.height - page.margin;

  function newPage() {
    if (commands.length) pages.push(commands);
    commands = [];
    y = page.height - page.margin;
  }

  commands.push({ text: docTitle, x: page.margin, y, size: 9, font: "regular" });
  y -= 24;

  for (const block of blocks) {
    const lineHeight = block.size * 1.35;
    const wrapped = wrapText(block.text, block.size);
    const blockHeight = wrapped.length * lineHeight + block.gap;
    if (y - blockHeight < page.margin) newPage();
    for (const line of wrapped) {
      if (line) commands.push({ text: line, x: page.margin, y, size: block.size, font: block.font });
      y -= lineHeight;
    }
    y -= block.gap;
  }
  if (commands.length) pages.push(commands);
  return pages;
}

function buildPdf(pages) {
  const objects = [];
  const add = (body) => {
    objects.push(body);
    return objects.length;
  };

  const catalogId = add("<< /Type /Catalog /Pages 2 0 R >>");
  const pagesId = add("");
  const fontRegularId = add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>");
  const fontBoldId = add("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>");
  const fontMonoId = add("<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>");
  const pageIds = [];

  for (const pageCommands of pages) {
    const stream = pageCommands
      .map((cmd) => `BT /${fonts[cmd.font]} ${cmd.size} Tf ${cmd.x} ${cmd.y.toFixed(2)} Td (${escapePdf(cmd.text)}) Tj ET`)
      .join("\n");
    const streamId = add(`<< /Length ${Buffer.byteLength(stream)} >>\nstream\n${stream}\nendstream`);
    const pageId = add(
      `<< /Type /Page /Parent ${pagesId} 0 R /MediaBox [0 0 ${page.width} ${page.height}] ` +
        `/Resources << /Font << /F1 ${fontRegularId} 0 R /F2 ${fontBoldId} 0 R /F3 ${fontMonoId} 0 R >> >> ` +
        `/Contents ${streamId} 0 R >>`,
    );
    pageIds.push(pageId);
  }

  objects[pagesId - 1] = `<< /Type /Pages /Kids [${pageIds.map((id) => `${id} 0 R`).join(" ")}] /Count ${pageIds.length} >>`;

  let pdf = "%PDF-1.4\n";
  const offsets = [0];
  objects.forEach((body, index) => {
    offsets.push(Buffer.byteLength(pdf));
    pdf += `${index + 1} 0 obj\n${body}\nendobj\n`;
  });
  const xref = Buffer.byteLength(pdf);
  pdf += `xref\n0 ${objects.length + 1}\n0000000000 65535 f \n`;
  for (let i = 1; i < offsets.length; i++) {
    pdf += `${String(offsets[i]).padStart(10, "0")} 00000 n \n`;
  }
  pdf += `trailer\n<< /Size ${objects.length + 1} /Root ${catalogId} 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
  return Buffer.from(pdf, "binary");
}

fs.mkdirSync(outDir, { recursive: true });

const markdownFiles = walk(root);
for (const file of markdownFiles) {
  const markdown = fs.readFileSync(file, "utf8");
  const title = titleFrom(file, markdown);
  const blocks = normaliseMarkdown(markdown);
  const pages = makePages(blocks, title);
  const relative = path.relative(root, file);
  const output = path.join(outDir, relative).replace(/\.md$/i, ".pdf");
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, buildPdf(pages));
  console.log(path.relative(process.cwd(), output));
}
