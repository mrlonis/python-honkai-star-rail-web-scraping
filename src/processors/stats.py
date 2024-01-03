"""This module contains the logic for the get_stats processor."""
from bs4 import BeautifulSoup, ResultSet, Tag

from src.character_data import CharacterData

CRIT_RATE = "CRIT Rate"
CRIT_DAMAGE = "CRIT DMG"
CRIT_RATE_AND_DAMAGE = "CRIT Rate / CRIT DMG"


def _body_stats(raw_stats: str | None, character_data: CharacterData):
    """Process the body stats."""
    if raw_stats is None:
        return
    split_data = raw_stats.split("/")
    i = 0
    contains_crit_rate_and_crit_damage = False
    while i < len(split_data):
        stat = split_data[i].strip()
        if i == 0:
            if stat == CRIT_RATE:
                if i + 1 < len(split_data) and split_data[i + 1].strip() == CRIT_DAMAGE:
                    character_data.body_main_stat_one = CRIT_RATE_AND_DAMAGE
                    i += 1
                    contains_crit_rate_and_crit_damage = True
            else:
                character_data.body_main_stat_one = stat
        elif i == 1:
            if stat == CRIT_RATE:
                if i + 1 < len(split_data) and split_data[i + 1].strip() == CRIT_DAMAGE:
                    character_data.body_main_stat_two = CRIT_RATE_AND_DAMAGE
                    i += 1
                    contains_crit_rate_and_crit_damage = True
            else:
                character_data.body_main_stat_two = stat
        elif i == 2 and contains_crit_rate_and_crit_damage:
            character_data.body_main_stat_two = stat
        else:
            raise ValueError("Body stats has more than two listed")
        i += 1


def _feet_stats(raw_stats: str | None, character_data: CharacterData):
    """Process the feet stats."""
    if raw_stats is None:
        return
    split_data = raw_stats.split("/")
    i = 0
    while i < len(split_data):
        stat = split_data[i].strip()
        if i == 0:
            character_data.feet_main_stat_one = stat
        elif i == 1:
            character_data.feet_main_stat_two = stat
        else:
            raise ValueError("Feet stats has more than two listed")
        i += 1


def _link_rope_stats(raw_stats: str | None, character_data: CharacterData):
    """Process the link rope stats."""
    if raw_stats is None:
        return
    split_data = raw_stats.split("/")
    i = 0
    while i < len(split_data):
        stat: str | None = split_data[i].strip()
        if stat == "Speed":
            stat = None
        if stat == "Energy Recharge Rate":
            stat = "Energy Regen Rate"
        if i == 0:
            character_data.link_rope_main_stat_one = stat
        elif i == 1:
            character_data.link_rope_main_stat_two = stat
        else:
            raise ValueError("Link rope stats has more than two listed")
        i += 1


def _substats(substats_raw: list[str], character_data: CharacterData):
    """Process the substats."""
    if not substats_raw:
        return
    i = 0
    while i < len(substats_raw):
        stat = substats_raw[i].strip()
        if stat == "Effect RES":
            stat = "Effect Res"
        if i == 0:
            character_data.substat_one = stat
        elif i == 1:
            character_data.substat_two = stat
        elif i == 2:
            character_data.substat_three = stat
        elif i == 3:
            character_data.substat_four = stat
        else:
            raise ValueError("Substats has more than four listed")
        i += 1


def get_stats(soup: BeautifulSoup, character_data: CharacterData):
    """Get the stats of the character."""
    character_stats: ResultSet[Tag] = soup.find_all("div", {"class": "character-info-stats-item"})
    print(character_stats)
    body_stats_raw: str | None = None
    feet_stats_raw: str | None = None
    planar_sphere_stats_raw: str | None = None
    link_rope_stats_raw: str | None = None
    substats: list[str] | None = None
    i = 0
    while i < len(character_stats):
        print(i)
        print(character_stats[i].text)
        i += 1
    if len(character_stats) >= 5:
        body_stats_raw = character_stats[0].text.split("Body: ")[1]
        print(f"body_stats_raw: {body_stats_raw}")
        feet_stats_raw = character_stats[1].text.split("Feet: ")[1]
        print(f"feet_stats_raw: {feet_stats_raw}")
        planar_sphere_stats_raw = character_stats[2].text.split("Planar Sphere: ")[1]
        print(f"planar_sphere_stats_raw: {planar_sphere_stats_raw}")
        link_rope_stats_raw = character_stats[3].text.split("Link Rope: ")[1]
        print(f"link_rope_stats_raw: {link_rope_stats_raw}")

        substats = []
        substats_counter = 4
        while substats_counter < len(character_stats):
            substats.append(character_stats[substats_counter].text)
            substats_counter += 1
        print(f"substats: {substats}")
    else:
        error_message = f"Character stats not found for {character_data.name}."
        print(f"ERROR: {error_message}")
        raise ValueError(error_message)

    _body_stats(body_stats_raw, character_data)
    _feet_stats(feet_stats_raw, character_data)
    character_data.planar_sphere_main_stat = planar_sphere_stats_raw.strip()
    _link_rope_stats(link_rope_stats_raw, character_data)
    _substats(substats, character_data)
