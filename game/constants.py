"""Gedeelde spelconstanten voor Treasure Run."""

from typing import Final

MIN_PLAYERS: Final[int] = 2
MAX_PLAYERS: Final[int] = 5
PATH_SPACES: Final[int] = 12
START_POSITION: Final[int] = 6

PLAYER_COLOR_HEX: Final[dict[str, str]] = {
    "Rood": "#E74C3C",
    "Blauw": "#3498DB",
    "Groen": "#27AE60",
    "Geel": "#F1C40F",
    "Paars": "#8E44AD",
}
