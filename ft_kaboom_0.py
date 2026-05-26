import alchemy.grimoire.light_spellbook as light
import alchemy.grimoire.light_validator as validator

ingredients = ", ".join(light.light_spell_allowed_ingredients())
validated = validator.validate_ingredients(ingredients)
print(light.light_spell_record("Fantasy", validated))
