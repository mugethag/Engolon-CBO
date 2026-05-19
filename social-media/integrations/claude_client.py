import os
import anthropic

_client = None

def get_client() -> anthropic.Anthropic:
    """Get or create the Anthropic API client (singleton)."""
    global _client
    if _client is None:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
        _client = anthropic.Anthropic(api_key=api_key)
    return _client

def complete(system: str, user: str,
             model: str = 'claude-sonnet-4-6',
             max_tokens: int = 2048) -> str:
    """Send a message to Claude and return the text response."""
    client = get_client()
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{'role': 'user', 'content': user}]
    )
    if not response.content or not hasattr(response.content[0], 'text'):
        raise ValueError(f"No text content in Claude response (model={model})")
    return response.content[0].text
