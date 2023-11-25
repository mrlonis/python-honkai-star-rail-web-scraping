"""This module contains the tests for the scrape_web.py script."""
from rich import print as pretty_print

from src.character_input import characters_list
from src.scrape_web import build_characters_csv, scrape_web


def test_scrape_web():
    """Test the scrape_web function."""
    print("test_scrape_web(): Starting...")
    character_data = scrape_web(character_input=characters_list[0], make_server_call=False)
    assert character_data is not None
    pretty_print(character_data)
    print(character_data.to_csv())
    print("test_scrape_web(): Finished.")


def test_build_characters_csv():
    """Test the build_characters_csv function."""
    print("test_build_characters_csv(): Starting...")
    build_characters_csv(make_server_call=False)
    print("test_build_characters_csv(): Finished.")
