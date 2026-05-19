import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.retry import with_retry

def test_succeeds_on_first_try():
    calls = []
    @with_retry(max_attempts=3, base_delay=0)
    def fn():
        calls.append(1)
        return "ok"
    assert fn() == "ok"
    assert len(calls) == 1

def test_retries_then_succeeds():
    calls = []
    @with_retry(max_attempts=3, base_delay=0)
    def fn():
        calls.append(1)
        if len(calls) < 3:
            raise ValueError("not yet")
        return "done"
    assert fn() == "done"
    assert len(calls) == 3

def test_raises_after_max_attempts():
    @with_retry(max_attempts=3, base_delay=0)
    def fn():
        raise RuntimeError("always fails")
    with pytest.raises(RuntimeError, match="always fails"):
        fn()

def test_only_retries_specified_exceptions():
    calls = []
    @with_retry(max_attempts=3, base_delay=0, exceptions=(ValueError,))
    def fn():
        calls.append(1)
        raise TypeError("wrong type")
    with pytest.raises(TypeError):
        fn()
    assert len(calls) == 1  # did not retry
