"""This module contains the logic for the get_combat_path processor."""
from bs4 import BeautifulSoup, Tag

from src.character_data import CharacterData


def _sanitize_combat_path(combat_path: str) -> str:
    """Sanitize the combat path."""
    if combat_path == "The Hunt":
        return combat_path
    return combat_path.split("The ")[1]


def get_combat_path(soup: BeautifulSoup, character_data: CharacterData):
    """Get the combat path of the character."""
    combat_path_result = soup.find("div", {"class": "character-info-path"})
    combat_path: str | None = None
    if combat_path_result and isinstance(combat_path_result, Tag):
        combat_path = combat_path_result.text.strip()
        print(f"Combat Path: {combat_path}")
        character_data.combat_path_id = _sanitize_combat_path(combat_path)
    else:
        error_message = f"Combat Path not found for {character_data.name}."
        print(f"ERROR: {error_message}")
        raise ValueError(error_message)
