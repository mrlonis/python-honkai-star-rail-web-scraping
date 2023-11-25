"""This module contains the logic for the get_rarity processor."""
from bs4 import BeautifulSoup, Tag

from src.character_data import CharacterData


def get_rarity(soup: BeautifulSoup, character_data: CharacterData):
    """Get the rarity of the character."""
    rarity_result = soup.find("img", {"class": "character-info-portrait"})
    rarity: int | None = None
    if rarity_result and isinstance(rarity_result, Tag):
        rarity = int(rarity_result.attrs["class"][1].split("-")[1])
        character_data.rarity = rarity
    else:
        error_message = f"Rarity not found for {character_data.name}."
        print(f"ERROR: {error_message}")
        raise ValueError(error_message)
