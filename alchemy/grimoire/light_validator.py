def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    validity = "VALID" if any(item.lower() in allowed for item in ingredients.split(", ")) else "INVALID"
    return f"{ingredients} - {validity}"