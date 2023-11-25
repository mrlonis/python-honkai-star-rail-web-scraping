"""This module contains the logic for the get_stats processor."""
# from bs4 import BeautifulSoup, ResultSet, Tag

# from src.character_data import CharacterData

# CRIT_RATE = "CRIT Rate"
# CRIT_DAMAGE = "CRIT DMG"
# CRIT_RATE_AND_DAMAGE = "CRIT Rate / CRIT DMG"


# def _sanitize_stat(stat: str, stat_type: str | None = None) -> str:
#     """Sanitize the stat."""
#     if "Elemental Master" == stat:
#         return "Elemental Mastery"
#     if "Energy Rechage" == stat:
#         return "Energy Recharge"
#     if "Crit Rate" == stat:
#         return CRIT_RATE
#     if "HP" == stat and stat_type == "circlet":
#         return "HP%"
#     return stat


# def _process_sands_stats(sands_stats_raw: str | None, character_data: CharacterData):
#     """Process the sands stats."""
#     if sands_stats_raw is None:
#         return
#     split_data = sands_stats_raw.split("/")
#     print(split_data)
#     i = 0
#     while i < len(split_data):
#         if i == 0:
#             character_data.sands_stat_one = _sanitize_stat(split_data[i].strip())
#         elif i == 1:
#             character_data.sands_stat_two = _sanitize_stat(split_data[i].strip())
#         elif i == 2:
#             character_data.sands_stat_three = _sanitize_stat(split_data[i].strip())
#         i += 1


# def _goblet_stats(goblet_stats_raw: str | None, character_data: CharacterData):
#     """Process the goblet stats."""
#     if not goblet_stats_raw:
#         return
#     split_data = goblet_stats_raw.split("/")
#     print(split_data)
#     i = 0
#     while i < len(split_data):
#         if i == 0:
#             character_data.goblet_stat_one = _sanitize_stat(split_data[i].strip())
#         elif i == 1:
#             character_data.goblet_stat_two = _sanitize_stat(split_data[i].strip())
#         elif i == 2:
#             character_data.goblet_stat_three = _sanitize_stat(split_data[i].strip())
#         i += 1


# def _crit_rate_and_damage(circlet_stats_raw: str):
#     """Process the goblet stats."""
#     split_data = circlet_stats_raw.split("/")
#     new_data: list[str] = []
#     split_length = len(split_data)
#     i = 0
#     while i < split_length:
#         if i == 0:
#             value = _sanitize_stat(split_data[i].strip())
#             if split_length > 1 and value == CRIT_RATE:
#                 next_value = _sanitize_stat(split_data[i + 1].strip())
#                 if next_value == CRIT_DAMAGE:
#                     value = CRIT_RATE_AND_DAMAGE
#                     i += 1
#             new_data.append(value)
#         elif i == 1:
#             value = _sanitize_stat(split_data[i].strip())
#             if split_length > 2 and value == CRIT_RATE:
#                 next_value = _sanitize_stat(split_data[i + 1].strip())
#                 if next_value == CRIT_DAMAGE:
#                     value = CRIT_RATE_AND_DAMAGE
#                     i += 1
#             new_data.append(value)
#         elif i == 2:
#             value = _sanitize_stat(split_data[i].strip())
#             if split_length > 3 and value == CRIT_RATE:
#                 next_value = _sanitize_stat(split_data[i + 1].strip())
#                 if next_value == CRIT_DAMAGE:
#                     value = CRIT_RATE_AND_DAMAGE
#                     i += 1
#             new_data.append(value)
#         i += 1
#     return new_data


# def _circlet_stats(circlet_stats_raw: str | None, character_data: CharacterData):
#     """Process the circlet stats."""
#     if not circlet_stats_raw:
#         return
#     split_data = _crit_rate_and_damage(circlet_stats_raw)
#     split_length = len(split_data)
#     print(split_data)
#     i = 0
#     while i < split_length:
#         if i == 0:
#             character_data.circlet_stat_one = _sanitize_stat(split_data[i].strip(), stat_type="circlet")
#         elif i == 1:
#             character_data.circlet_stat_two = _sanitize_stat(split_data[i].strip(), stat_type="circlet")
#         elif i == 2:
#             character_data.circlet_stat_three = _sanitize_stat(split_data[i].strip(), stat_type="circlet")
#         i += 1


# def _substats(substats_raw: str | None, character_data: CharacterData):
#     """Process the substats."""
#     if not substats_raw:
#         return
#     split_data = substats_raw.split(">")
#     i = 0
#     while i < len(split_data):
#         if i == 0:
#             character_data.substat_one = _sanitize_stat(split_data[i].strip())
#         elif i == 1:
#             character_data.substat_two = _sanitize_stat(split_data[i].strip())
#         elif i == 2:
#             character_data.substat_three = _sanitize_stat(split_data[i].strip())
#         i += 1


# def get_stats(soup: BeautifulSoup, character_data: CharacterData):
#     """Get the stats of the character."""
#     character_stats: ResultSet[Tag] = soup.find_all("div", {"class": "character-stats-item"})
#     sands_stats_raw: str | None = None
#     goblet_stats_raw: str | None = None
#     circlet_stats_raw: str | None = None
#     substats_raw: str | None = None
#     if len(character_stats) == 4:
#         sands_stats_raw = character_stats[0].text.split("Sands: ")[1]
#         print(sands_stats_raw)
#         goblet_stats_raw = character_stats[1].text.split("Goblet: ")[1]
#         print(goblet_stats_raw)
#         circlet_stats_raw = character_stats[2].text.split("Circlet: ")[1]
#         print(circlet_stats_raw)
#         substats_raw = character_stats[3].text.split("Substats: ")[1]
#         print(substats_raw)
#     else:
#         error_message = f"Character stats not found for {character_data.name}."
#         print(f"ERROR: {error_message}")
#         raise ValueError(error_message)

#     _process_sands_stats(sands_stats_raw, character_data)
#     _goblet_stats(goblet_stats_raw, character_data)
#     _circlet_stats(circlet_stats_raw, character_data)
#     _substats(substats_raw, character_data)
