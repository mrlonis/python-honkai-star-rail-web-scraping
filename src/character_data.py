"""This module contains the character data model information."""
from pydantic import BaseModel


def _convert_field_to_csv(field: str | int | None) -> str:
    """Convert the field to a CSV string."""
    if field is None:
        return ""
    if isinstance(field, int):
        return str(field)
    if "," in field:
        return f'"{field}"'
    if '"' in field:
        return f'""{field}""'
    return field


class CharacterData(BaseModel):
    """Character data model."""

    name: str
    image_url: str | None = None
    rarity: int = 0
    combat_path_id: str = ""
    combat_type_id: str = ""

    body_main_stat_one: str | None = None
    body_main_stat_two: str | None = None
    feet_main_stat_one: str | None = None
    feet_main_stat_two: str | None = None
    planar_sphere_main_stat: str | None = None
    link_rope_main_stat_one: str | None = None
    link_rope_main_stat_two: str | None = None
    substat_one: str | None = None
    substat_two: str | None = None
    substat_three: str | None = None
    substat_four: str | None = None
    relic_set_one_id_first: str | None = None
    relic_set_one_id_second: str | None = None
    relic_set_two_id_first: str | None = None
    relic_set_two_id_second: str | None = None
    relic_set_three_id_first: str | None = None
    relic_set_three_id_second: str | None = None
    ornament_set_one_id: str | None = None
    ornament_set_two_id: str | None = None
    ornament_set_three_id: str | None = None
    light_cone_one_id: str | None = None
    light_cone_two_id: str | None = None
    light_cone_three_id: str | None = None
    light_cone_four_id: str | None = None
    light_cone_five_id: str | None = None

    def to_csv(self):
        """Convert the character data to a CSV string."""
        return (
            f"{_convert_field_to_csv(self.name)},"
            + f"{_convert_field_to_csv(self.image_url)},"
            + f"{_convert_field_to_csv(self.rarity)},"
            + f"{_convert_field_to_csv(self.combat_path_id)},"
            + f"{_convert_field_to_csv(self.combat_type_id)},"
            + f"{_convert_field_to_csv(self.body_main_stat_one)},"
            + f"{_convert_field_to_csv(self.body_main_stat_two)},"
            + f"{_convert_field_to_csv(self.feet_main_stat_one)},"
            + f"{_convert_field_to_csv(self.feet_main_stat_two)},"
            + f"{_convert_field_to_csv(self.planar_sphere_main_stat)},"
            + f"{_convert_field_to_csv(self.link_rope_main_stat_one)},"
            + f"{_convert_field_to_csv(self.link_rope_main_stat_two)},"
            + f"{_convert_field_to_csv(self.substat_one)},"
            + f"{_convert_field_to_csv(self.substat_two)},"
            + f"{_convert_field_to_csv(self.substat_three)},"
            + f"{_convert_field_to_csv(self.substat_four)},"
            + f"{_convert_field_to_csv(self.relic_set_one_id_first)},"
            + f"{_convert_field_to_csv(self.relic_set_one_id_second)},"
            + f"{_convert_field_to_csv(self.relic_set_two_id_first)},"
            + f"{_convert_field_to_csv(self.relic_set_two_id_second)},"
            + f"{_convert_field_to_csv(self.relic_set_three_id_first)},"
            + f"{_convert_field_to_csv(self.relic_set_three_id_second)},"
            + f"{_convert_field_to_csv(self.ornament_set_one_id)},"
            + f"{_convert_field_to_csv(self.ornament_set_two_id)},"
            + f"{_convert_field_to_csv(self.ornament_set_three_id)},"
            + f"{_convert_field_to_csv(self.light_cone_one_id)},"
            + f"{_convert_field_to_csv(self.light_cone_two_id)},"
            + f"{_convert_field_to_csv(self.light_cone_three_id)},"
            + f"{_convert_field_to_csv(self.light_cone_four_id)},"
            + f"{_convert_field_to_csv(self.light_cone_five_id)}"
        )
