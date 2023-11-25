"""This module contains the character data information."""
from pydantic import BaseModel


class CharacterInput(BaseModel):
    """Character data model."""

    name: str
    url_name: str | None = None
    skip: bool = False


characters_list: list[CharacterInput] = [
    CharacterInput(name="March 7th", url_name="march7th"),
    CharacterInput(name="Dan Heng", url_name="danheng"),
    CharacterInput(name="Himeko"),
    CharacterInput(name="Welt"),
    CharacterInput(name="Kafka"),
    CharacterInput(name="Silver Wolf", url_name="silverwolf"),
    CharacterInput(name="Arlan"),
    CharacterInput(name="Asta"),
    CharacterInput(name="Herta"),
    CharacterInput(name="Bronya"),
    CharacterInput(name="Seele"),
    CharacterInput(name="Serval"),
    CharacterInput(name="Gepard"),
    CharacterInput(name="Natasha"),
    CharacterInput(name="Pela"),
    CharacterInput(name="Clara"),
    CharacterInput(name="Sampo"),
    CharacterInput(name="Hook"),
    CharacterInput(name="Lynx"),
    CharacterInput(name="Luka"),
    CharacterInput(name="Topaz & Numby", url_name="topazandnumby"),
    CharacterInput(name="Qingque"),
    CharacterInput(name="Tingyun"),
    CharacterInput(name="Luocha"),
    CharacterInput(name="Jing Yuan", url_name="jingyuan"),
    CharacterInput(name="Blade"),
    CharacterInput(name="Sushang"),
    CharacterInput(name="Yukong"),
    CharacterInput(name="Fu Xuan", url_name="fuxuan"),
    CharacterInput(name="Yanqing"),
    CharacterInput(name="Guinaifen"),
    CharacterInput(name="Bailu"),
    CharacterInput(name="Jingliu"),
    CharacterInput(name="Dan Heng - Imbibitor Lunae", url_name="danheng-imbibitorlunae"),
    CharacterInput(name="Xueyi", skip=True),
    CharacterInput(name="Hanya"),
    CharacterInput(name="Huohuo"),
    CharacterInput(name="Argenti"),
    CharacterInput(name="Dr. Ratio", skip=True),
    CharacterInput(name="Trailblazer (Physical)", url_name="trailblazer(physical)"),
    CharacterInput(name="Trailblazer (Fire)", url_name="trailblazer(fire)"),
]
