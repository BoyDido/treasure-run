"""Bordrepresentatie voor Treasure Run."""

from dataclasses import dataclass

from .constants import BOARD_COLUMNS, BOARD_ROWS, START_POSITION
from .models import Player


@dataclass(frozen=True, slots=True)
class Board:
    """Een minimalistisch rechthoekig spelbord met een centraal startvak."""

    rows: int = BOARD_ROWS
    columns: int = BOARD_COLUMNS
    start_position: tuple[int, int] = START_POSITION

    def contains(self, position: tuple[int, int]) -> bool:
        """Controleer of een positie binnen de grenzen van het bord valt."""
        row, column = position
        return 0 <= row < self.rows and 0 <= column < self.columns

    def players_at(self, players: list[Player], position: tuple[int, int]) -> list[Player]:
        """Geef alle spelers die op de opgegeven positie staan."""
        return [player for player in players if player.position == position]
