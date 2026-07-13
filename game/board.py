"""Bordrepresentatie voor Treasure Run."""

from dataclasses import dataclass

from .constants import PATH_SPACES, START_POSITION
from .models import Player


@dataclass(frozen=True, slots=True)
class Board:
    """Een speelbord met twaalf genummerde padvakken."""

    path_spaces: int = PATH_SPACES
    start_position: int = START_POSITION

    def contains(self, position: int) -> bool:
        """Controleer of een positie een geldig padvak is."""
        return 1 <= position <= self.path_spaces

    def move(self, position: int, direction: int, steps: int) -> tuple[int, int]:
        """Verplaats een speler over het pad en keer om aan beide uiteinden.

        Een speler die vak 12 bereikt gaat bij de volgende stap naar vak 11.
        Een speler die vak 1 bereikt gaat bij de volgende stap naar vak 2.

        Args:
            position: Het huidige padvak van de speler.
            direction: De bewegingsrichting: ``1`` naar vak 12 of ``-1`` naar vak 1.
            steps: Het aantal vakken dat de speler vooruit beweegt.

        Returns:
            De nieuwe positie en richting van de speler.

        Raises:
            ValueError: Als positie ongeldig is of als het aantal stappen negatief is.
        """
        if not self.contains(position):
            raise ValueError("De huidige positie ligt niet op het pad.")
        if direction not in (-1, 1):
            raise ValueError("De richting moet 1 of -1 zijn.")
        if steps < 0:
            raise ValueError("Het aantal stappen kan niet negatief zijn.")

        for _ in range(steps):
            if position == self.path_spaces:
                direction = -1
            elif position == 1:
                direction = 1
            position += direction
        return position, direction

    def players_at(self, players: list[Player], position: int) -> list[Player]:
        """Geef alle spelers die op de opgegeven positie staan."""
        return [player for player in players if player.position == position]
