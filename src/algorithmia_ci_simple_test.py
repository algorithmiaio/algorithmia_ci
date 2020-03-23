from . import algorithmia_ci_simple

def test_algorithmia_ci_simple():
    assert algorithmia_ci_simple.apply("Jane") == "hello Jane"
