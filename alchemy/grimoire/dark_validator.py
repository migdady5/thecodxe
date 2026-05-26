def validate_ingredients(ingredients: str) -> str:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    is_valid = any(item.lower() in allowed for item in ingredients.split(", "))
    validity = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {validity}"
