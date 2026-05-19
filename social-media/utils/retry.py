import time
import functools

def with_retry(max_attempts=3, base_delay=1.0, exceptions=(Exception,)):
    """Retry decorator with exponential backoff. Delay = base_delay * 2^attempt."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except exceptions:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(base_delay * (2 ** attempt))
        return wrapper
    return decorator
