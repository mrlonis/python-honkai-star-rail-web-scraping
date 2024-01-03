"""This module contains the logic for the get_relics processor."""
from bs4 import BeautifulSoup, ResultSet, Tag

from src.character_data import CharacterData


def _process_relics_html(soup: BeautifulSoup, relics: list[list[str]], ornaments: list[str], light_cones: list[str]):
    """Process the relics html into data structures."""
    # 0 is the initial value and represents relic
    # 1 is the next increment and also represents a relic, but not the first relic
    # 2 represents ornament
    # 3 represents light cone
    relic_ornament_or_light_cone = 0
    results: ResultSet[Tag] = soup.find_all("div", {"class": "character-info-weapon"})
    for result in results:
        print(f"result: {result}")
        weapon_rank = result.find("div", {"class": "character-info-weapon-rank"})
        print(f"weapon_rank: {weapon_rank}")
        weapon_name: ResultSet[Tag] = result.find_all("div", {"class": "character-info-weapon-name"})
        print(f"weapon_name: {weapon_name}")
        print(" ")

        if (weapon_rank is None or weapon_rank.text.strip() == "1") and relic_ornament_or_light_cone < 3:
            relic_ornament_or_light_cone += 1

        if relic_ornament_or_light_cone == 0:
            relic_set = []
            for weapon in weapon_name:
                relic_set.append(weapon.text.strip())
            relics.append(relic_set)
            relic_ornament_or_light_cone += 1
        elif relic_ornament_or_light_cone == 1:
            relic_set = []
            for weapon in weapon_name:
                relic_set.append(weapon.text.strip())
            relics.append(relic_set)
        elif relic_ornament_or_light_cone == 2:
            if len(weapon_name) > 1:
                raise ValueError("Ornament has more than one listed")
            ornaments.append(weapon_name[0].text.strip())
        elif relic_ornament_or_light_cone == 3:
            if len(weapon_name) > 1:
                raise ValueError("Light cone has more than one listed")
            light_cones.append(weapon_name[0].text.strip())


def _process_relics(relics: list[list[str]], character_data: CharacterData):
    """Process the relics data and assign to character data."""
    # pylint: disable=too-many-branches
    i = 0
    while i < len(relics):
        relic_set = relics[i]
        if i == 0:
            if len(relic_set) == 0:
                i += 1
                continue
            if len(relic_set) == 1:
                character_data.relic_set_one_id_first = relic_set[0]
            elif len(relic_set) == 2:
                character_data.relic_set_one_id_first = relic_set[0]
                character_data.relic_set_one_id_second = relic_set[1]
            else:
                raise ValueError("Relic set 1 has more than two listed")
        elif i == 1:
            if len(relic_set) == 0:
                i += 1
                continue
            if len(relic_set) == 1:
                character_data.relic_set_two_id_first = relic_set[0]
            elif len(relic_set) == 2:
                character_data.relic_set_two_id_first = relic_set[0]
                character_data.relic_set_two_id_second = relic_set[1]
            else:
                raise ValueError("Relic set 2 has more than two listed")
        elif i == 2:
            if len(relic_set) == 0:
                i += 1
                continue
            if len(relic_set) == 1:
                character_data.relic_set_three_id_first = relic_set[0]
            elif len(relic_set) == 2:
                character_data.relic_set_three_id_first = relic_set[0]
                character_data.relic_set_three_id_second = relic_set[1]
            else:
                raise ValueError("Relic set 3 has more than two listed")
        i += 1


def _process_ornaments(ornaments: list[str], character_data: CharacterData):
    """Process the ornaments data and assign to character data."""
    i = 0
    while i < len(ornaments):
        ornament = ornaments[i]
        if ornament == "Pan-Galactic Commercial Enterprise":
            ornament = "Pan-Cosmic Commercial Enterprise"
        if i == 0:
            character_data.ornament_set_one_id = ornament
        elif i == 1:
            character_data.ornament_set_two_id = ornament
        elif i == 2:
            character_data.ornament_set_three_id = ornament
        else:
            raise ValueError("Too many ornaments for character.")
        i += 1


def _process_light_cones(light_cones: list[str], character_data: CharacterData):
    """Process the light cones data and assign to character data."""
    i = 0
    while i < len(light_cones):
        light_cone = light_cones[i]
        if light_cone == "The Battle Isn't Over":
            light_cone = "But the Battle Isn't Over"
        if i == 0:
            character_data.light_cone_one_id = light_cone
        elif i == 1:
            character_data.light_cone_two_id = light_cone
        elif i == 2:
            character_data.light_cone_three_id = light_cone
        elif i == 3:
            character_data.light_cone_four_id = light_cone
        elif i == 4:
            character_data.light_cone_five_id = light_cone
        else:
            raise ValueError("Too many light cones for character.")
        i += 1


def get_relics_ornaments_and_light_cones(soup: BeautifulSoup, character_data: CharacterData):
    """Get the relics, ornaments, and light cones of the character."""
    relics: list[list[str]] = []
    ornaments: list[str] = []
    light_cones: list[str] = []
    _process_relics_html(soup, relics, ornaments, light_cones)
    print(f"relics: {relics}")
    print(f"ornaments: {ornaments}")
    print(f"light_cones: {light_cones}")
    _process_relics(relics, character_data)
    _process_ornaments(ornaments, character_data)
    _process_light_cones(light_cones, character_data)
