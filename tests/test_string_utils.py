from src.string_utils import title_case, snake_to_camel, reverse_words


def test_title_case():
    assert title_case("hello world") == "Hello World"
    assert title_case("HELLO WORLD") == "Hello World"
    assert title_case("hello   world") == "Hello World"


def test_snake_to_camel():
    assert snake_to_camel("hello_world") == "helloWorld"
    assert snake_to_camel("user_first_name") == "userFirstName"
    assert snake_to_camel("id") == "id"


def test_reverse_words():
    assert reverse_words("hello world") == "olleh dlrow"
    assert reverse_words("python") == "nohtyp"
    assert reverse_words("a b c") == "a b c"
