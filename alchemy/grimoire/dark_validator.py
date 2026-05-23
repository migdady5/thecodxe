def validate_ingredients(ingredients: str) -> str:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    validity = "VALID" if any(item.lower() in allowed for item in ingredients.split(", ")) else "INVALID"
    return f"{ingredients} - {validity}"