"""This module contains the logic for the get_combat_type processor."""

from bs4 import BeautifulSoup, Tag

from src.character_data import CharacterData


def get_combat_type(soup: BeautifulSoup, character_data: CharacterData):
    """Get the combat type of the character."""
    combat_type_result = soup.find("img", {"class": "character-info-element"})
    combat_type: str | None = None
    if combat_type_result and isinstance(combat_type_result, Tag):
        combat_type = combat_type_result.attrs["alt"].strip()
        print(f"Combat Type: {combat_type}")
    if combat_type:
        character_data.combat_type_id = combat_type
    else:
        error_message = f"Combat Type not found for {character_data.name}."
        print(f"ERROR: {error_message}")
        raise ValueError(error_message)
