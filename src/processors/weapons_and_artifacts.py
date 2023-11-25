"""This module contains the logic for the get_weapons_and_artifacts processor."""
# from bs4 import BeautifulSoup, ResultSet, Tag

# from src.character_data import CharacterData


# def _process_weapon_and_artifacts_html(soup: BeautifulSoup, weapons: list[str], artifacts: list[list[str]]):
#     """Process the weapons and artifacts html into data structures."""
#     # 0 is the initial value and represents weapon
#     # 1 is the next increment and also represents a weapon, but not the first weapon
#     # 2 represents artifact
#     weapon_or_artifact = 0
#     results: ResultSet[Tag] = soup.find_all("div", {"class": "character-build-weapon"})
#     for result in results:
#         weapon_rank = result.find("div", {"class": "character-build-weapon-rank"})
#         weapon_name: ResultSet[Tag] = result.find_all("div", {"class": "character-build-weapon-name"})

#         if weapon_rank and weapon_name:
#             weapon_rank_text = int(weapon_rank.text)

#             if weapon_rank_text == 1 and weapon_or_artifact == 0:
#                 if len(weapon_name) == 1:
#                     weapons.append(weapon_name[0].text)
#                 weapon_or_artifact += 1
#             elif weapon_rank_text == 1 and weapon_or_artifact == 1:
#                 if len(weapon_name) == 1:
#                     artifacts.append([weapon_name[0].text])
#                 elif len(weapon_name) == 2:
#                     artifacts.append([weapon_name[0].text, weapon_name[1].text])

#                 weapon_or_artifact += 1
#             elif weapon_or_artifact == 1:
#                 if len(weapon_name) == 1:
#                     weapons.append(weapon_name[0].text)
#             else:
#                 if len(weapon_name) == 1:
#                     artifacts.append([weapon_name[0].text])
#                 elif len(weapon_name) == 2:
#                     artifacts.append([weapon_name[0].text, weapon_name[1].text])


# def _sanitize_weapon_name(weapon_name: str) -> str:
#     """Sanitize the weapon name."""
#     new_weapon_name = (
#         weapon_name.replace("R1", "").replace("R2", "").replace("R3", "").replace("R4", "").replace("R5", "").strip()
#     )
#     if "The Catch" == new_weapon_name:
#         return '"The Catch"'
#     return new_weapon_name


# def _process_weapons(weapons: list[str], character_data: CharacterData):
#     """Process the weapons data and assign to character data."""
#     i = 0
#     while i < len(weapons):
#         if i == 0:
#             character_data.weapon_one_id = _sanitize_weapon_name(weapons[i])
#         elif i == 1:
#             character_data.weapon_two_id = _sanitize_weapon_name(weapons[i])
#         elif i == 2:
#             character_data.weapon_three_id = _sanitize_weapon_name(weapons[i])
#         elif i == 3:
#             character_data.weapon_four_id = _sanitize_weapon_name(weapons[i])
#         elif i == 4:
#             character_data.weapon_five_id = _sanitize_weapon_name(weapons[i])
#         else:
#             error_message = f"Too many weapons for {character_data.name}."
#             print(f"ERROR: {error_message}")
#             raise ValueError(error_message)
#         i += 1


# def _process_artifacts(artifacts: list[list[str]], character_data: CharacterData):
#     """Process artifacts data and assign to character data."""
#     # pylint: disable=too-many-branches
#     i = 0
#     while i < len(artifacts):
#         if i == 0:
#             if len(artifacts[i]) == 1:
#                 character_data.artifact_set_one_id_first = artifacts[i][0]
#             elif len(artifacts[i]) == 2:
#                 character_data.artifact_set_one_id_first = artifacts[i][0]
#                 character_data.artifact_set_one_id_second = artifacts[i][1]
#         elif i == 1:
#             if len(artifacts[i]) == 1:
#                 character_data.artifact_set_two_id_first = artifacts[i][0]
#             elif len(artifacts[i]) == 2:
#                 character_data.artifact_set_two_id_first = artifacts[i][0]
#                 character_data.artifact_set_two_id_second = artifacts[i][1]
#         elif i == 2:
#             if len(artifacts[i]) == 1:
#                 character_data.artifact_set_three_id_first = artifacts[i][0]
#             elif len(artifacts[i]) == 2:
#                 character_data.artifact_set_three_id_first = artifacts[i][0]
#                 character_data.artifact_set_three_id_second = artifacts[i][1]
#         elif i == 3:
#             if len(artifacts[i]) == 1:
#                 character_data.artifact_set_four_id_first = artifacts[i][0]
#             elif len(artifacts[i]) == 2:
#                 character_data.artifact_set_four_id_first = artifacts[i][0]
#                 character_data.artifact_set_four_id_second = artifacts[i][1]
#         elif i == 4:
#             if len(artifacts[i]) == 1:
#                 character_data.artifact_set_five_id_first = artifacts[i][0]
#             elif len(artifacts[i]) == 2:
#                 character_data.artifact_set_five_id_first = artifacts[i][0]
#                 character_data.artifact_set_five_id_second = artifacts[i][1]
#         else:
#             error_message = f"Too many artifacts for {character_data.name}."
#             print(f"ERROR: {error_message}")
#             raise ValueError(error_message)
#         i += 1


# def get_weapons_and_artifacts(soup: BeautifulSoup, character_data: CharacterData):
#     """Get the weapons and artifacts of the character."""
#     weapons: list[str] = []
#     artifacts: list[list[str]] = []
#     _process_weapon_and_artifacts_html(soup, weapons, artifacts)
#     _process_weapons(weapons, character_data)
#     _process_artifacts(artifacts, character_data)
