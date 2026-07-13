"""Hulpfuncties voor het voorbereiden van een nieuw spel."""

from .engine import GameEngine
from .models import GameState, PlayerColor


def create_game(player_details: list[tuple[str, PlayerColor]]) -> GameEngine:
    """Maak en start een spel met de opgegeven spelers.

    Args:
        player_details: Paren van spelersnaam en pionkleur.

    Returns:
        Een gestarte ``GameEngine``.
    """
    engine = GameEngine()
    engine.start_new_game(player_details)
    return engine


def setup_state(engine: GameEngine) -> GameState:
    """Geef de actuele speltoestand terug voor weergave of opslag."""
    return engine.state
