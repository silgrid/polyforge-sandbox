def greet(name: str) -> str:
    """Trim surrounding whitespace from name, defaulting blank names to world."""
    name = name.strip() or "world"
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    print(greet(sys.argv[1] if len(sys.argv) > 1 else "world"))
