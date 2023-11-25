"""This module contains the logic for the scrape_web.py script."""
import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
from rich import print as pretty_print

from .character_data import CharacterData
from .character_input import CharacterInput, characters_list
from .processors import get_combat_path, get_rarity  # , get_stats, get_weapon_type, get_weapons_and_artifacts


def build_characters_csv(make_server_call: bool = False):
    """Build the characters.csv file."""
    with open("output/characters.csv", "w", encoding="utf-8") as csv_file:
        # pylint: disable=line-too-long
        csv_file.write(
            "name,imageUrl,rarity,combatPathId,combatTypeId,bodyMainStatOne,bodyMainStatTwo,feetMainStatOne,feetMainStatTwo,planarSphereMainStat,linkRopeMainStatOne,linkRopeMainStatTwo,substatOne,substatTwo,substatThree,substatFour,relicSetOneIdFirst,relicSetOneIdSecond,relicSetTwoIdFirst,relicSetTwoIdSecond,relicSetThreeIdFirst,relicSetThreeIdSecond,ornamentSetOneId,ornamentSetTwoId,lightConeOneId,lightConeTwoId,lightConeThreeId,lightConeFourId,lightConeFiveId\n"  # noqa: E501
        )
        for character_input in characters_list:
            if not character_input.skip:
                character = scrape_web(character_input, make_server_call=make_server_call)
                csv_file.write(character.to_csv() + "\n")


def _build_url(character_input: CharacterInput):
    """Build the url."""
    url_path = character_input.url_name if character_input.url_name else character_input.name.lower()
    return "https://genshin.gg/star-rail/characters/" + url_path + "/"


def _build_sample_data_path(character_input: CharacterInput):
    """Build the sample data path."""
    url_path = character_input.url_name if character_input.url_name else character_input.name.lower()
    return "sample_data/" + url_path + ".html"


def scrape_web(character_input: CharacterInput, make_server_call=False):
    """Scrape the web for data."""
    if make_server_call:
        with urlopen(_build_url(character_input)) as page:  # nosec
            html = page.read().decode("utf-8")
            sample_data_path = _build_sample_data_path(character_input)
            with open(sample_data_path, "w", encoding="utf-8") as sample_data_file:
                sample_data_file.write(html)
    else:
        sample_data_path = _build_sample_data_path(character_input)
        if os.path.exists(sample_data_path):
            with open(sample_data_path, "r", encoding="utf-8") as file:
                html = file.read()
        else:
            with urlopen(_build_url(character_input)) as page:  # nosec
                html = page.read().decode("utf-8")
                with open(sample_data_path, "w", encoding="utf-8") as sample_data_file:
                    sample_data_file.write(html)

    soup = BeautifulSoup(html, "html.parser")
    character_data: CharacterData = CharacterData(name=character_input.name)

    get_rarity(soup, character_data)
    get_combat_path(soup, character_data)
    # get_weapon_type(soup, character_data)
    # get_stats(soup, character_data)
    # get_weapons_and_artifacts(soup, character_data)

    pretty_print(character_data)
    return character_data
