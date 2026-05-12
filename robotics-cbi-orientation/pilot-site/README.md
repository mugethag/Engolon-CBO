# Engolon Robotics Pilot Site

This is a lightweight static replacement for Moodle for Cohort 1.

## Pages

- `index.html` - public application and program page
- `portal.html` - learner portal with weekly resources
- `project-brief.html` - Week 4 final project instructions
- `admin.html` - admin tracker and report downloads

## Templates

- `templates/cohort-tracker.csv` - learner operations tracker
- `templates/application-review-rubric.csv` - screening rubric
- `templates/sponsor-report-template.md` - sponsor-ready cohort report format

## Course Downloads

The portal links to PDFs generated in:

```text
../course-mvp/pdfs/
```

Keep the `pilot-site` folder beside `course-mvp` when deploying so the PDF links continue to work.

## Application Form

The current form is static. On submit it:

1. Downloads a CSV row for the applicant.
2. Opens an email draft to `info@zawadilabs.com`.

For production, replace this with Tally, Airtable, Google Forms, or a server-side form endpoint.

## Deployment

For a simple VPS/static deployment, upload the full `robotics-cbi-orientation` folder, or upload both:

```text
pilot-site/
course-mvp/pdfs/
```

Then point the web root to `pilot-site/index.html` or copy the contents of `pilot-site` into the desired public web root while preserving access to the PDF paths.
