"""This module contains the logic for the get_weapon_type processor."""
# from bs4 import BeautifulSoup, Tag

# from src.character_data import CharacterData


# def get_weapon_type(soup: BeautifulSoup, character_data: CharacterData):
#     """Get the weapon type of the character."""
#     weapon_type_result = soup.find("div", {"class": "character-path"})
#     weapon_type: str | None = None
#     if weapon_type_result and isinstance(weapon_type_result, Tag):
#         weapon_type = weapon_type_result.text.strip()
#         character_data.weapon_type = weapon_type
#     else:
#         error_message = f"Weapon type not found for {character_data.name}."
#         print(f"ERROR: {error_message}")
#         raise ValueError(error_message)
