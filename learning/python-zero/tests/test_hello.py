from src.hello import greeting


def test_greeting_uses_name():
    assert greeting("Nandu") == "Hello, Nandu!"


def test_greeting_handles_empty_name():
    assert greeting("") == "Hello, !"
