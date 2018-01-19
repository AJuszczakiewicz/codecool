def greet(name):
    """Greets person. Greets Johnny in special way."""
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)