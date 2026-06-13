import os
from openai import OpenAI

_client = None


def get_client() -> OpenAI:
    """Get or create the OpenAI API client (singleton)."""
    global _client
    if _client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        _client = OpenAI(api_key=api_key)
    return _client


def complete(system: str, user: str,
             model: str | None = None,
             max_tokens: int = 2048) -> str:
    """Send a prompt to OpenAI and return the text response."""
    client = get_client()
    selected_model = model or os.environ.get("OPENAI_MODEL") or "gpt-4.1-mini"
    response = client.responses.create(
        model=selected_model,
        instructions=system,
        input=user,
        max_output_tokens=max_tokens,
    )
    text = getattr(response, "output_text", None)
    if not text:
        raise ValueError(f"No text content in OpenAI response (model={selected_model})")
    return text
