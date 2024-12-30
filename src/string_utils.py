def title_case(text: str) -> str:
    """Convert string to title case, handling special cases."""
    return " ".join(word.capitalize() for word in text.split())


def snake_to_camel(text: str) -> str:
    """Convert snake_case to camelCase."""
    components = text.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def reverse_words(text: str) -> str:
    """Reverse the words in a string while maintaining word order."""
    return " ".join(word[::-1] for word in text.split())
