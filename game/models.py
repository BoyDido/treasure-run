"""Datamodellen voor de eerste sprint van Treasure Run."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4

from .cards import ActionCard
from .constants import START_POSITION


class PlayerColor(str, Enum):
    """De beschikbare pionkleuren."""

    RED = "Rood"
    BLUE = "Blauw"
    GREEN = "Groen"
    YELLOW = "Geel"
    PURPLE = "Paars"


@dataclass(slots=True)
class Player:
    """Een speler met een naam, kleur en positie op het bord."""

    name: str
    color: PlayerColor
    position: int = START_POSITION
    direction: int = 1
    hand: list[ActionCard] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(slots=True)
class GameState:
    """De bewaarbare toestand van een gestart spel."""

    players: list[Player]
    is_started: bool = False
    current_player_index: int = 0

    @property
    def current_player(self) -> Player | None:
        """Geef de speler die aan de beurt is, of ``None`` voor een leeg spel."""
        if not self.players:
            return None
        return self.players[self.current_player_index]
