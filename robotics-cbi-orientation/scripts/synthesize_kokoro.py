import inspect
import sys

import kokoro_onnx
import soundfile as sf


def main():
    model_path = sys.argv[1]
    voices_path = sys.argv[2]
    text_path = sys.argv[3]
    voice = sys.argv[4]
    speed = float(sys.argv[5])
    output_path = sys.argv[6]
    lang = sys.argv[7] if len(sys.argv) > 7 else ""

    with open(text_path, "r", encoding="utf-8") as handle:
        text = handle.read()

    model = kokoro_onnx.Kokoro(model_path, voices_path)
    kwargs = {"voice": voice, "speed": speed}
    if lang and "lang" in inspect.signature(model.create).parameters:
        kwargs["lang"] = lang

    samples, sample_rate = model.create(text, **kwargs)
    sf.write(output_path, samples, sample_rate)


if __name__ == "__main__":
    main()
