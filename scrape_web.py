"""This module contains the logic for the scrape_web.py script."""

from src.scrape_web import build_characters_csv

MAKE_SERVER_CALL = False

build_characters_csv(make_server_call=MAKE_SERVER_CALL)
