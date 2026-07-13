"""Spelcoördinatie voor Treasure Run."""

from __future__ import annotations

from dataclasses import dataclass, field

from .board import Board
from .cards import ActionDeck
from .constants import MAX_PLAYERS, MIN_PLAYERS
from .models import GameState, Player, PlayerColor


@dataclass
class GameEngine:
    """Beheert het aanmaken en de basistoestand van een Treasure Run-spel."""

    board: Board = field(default_factory=Board)
    state: GameState = field(default_factory=lambda: GameState(players=[]))
    action_deck: ActionDeck = field(default_factory=ActionDeck)

    def start_new_game(self, player_details: list[tuple[str, PlayerColor]]) -> GameState:
        """Start een nieuw spel met unieke spelers en plaats ze op het startvak.

        Args:
            player_details: Paren van spelersnaam en gekozen kleur.

        Returns:
            De nieuw aangemaakte speltoestand.

        Raises:
            ValueError: Als het aantal spelers, een naam of een kleur ongeldig is.
        """
        self._validate_player_details(player_details)
        players = [
            Player(name=name.strip(), color=color, position=self.board.start_position)
            for name, color in player_details
        ]
        self.action_deck = ActionDeck()
        self.action_deck.shuffle()
        for player in players:
            player.hand = self.action_deck.draw(4)

        self.state = GameState(players=players, is_started=True)
        return self.state

    def reset_game(self) -> None:
        """Wis de huidige speltoestand zodat een nieuw spel kan worden voorbereid."""
        self.state = GameState(players=[])

    @staticmethod
    def _validate_player_details(player_details: list[tuple[str, PlayerColor]]) -> None:
        """Valideer de invoer die nodig is om een spel te starten."""
        if not MIN_PLAYERS <= len(player_details) <= MAX_PLAYERS:
            raise ValueError(f"Kies tussen {MIN_PLAYERS} en {MAX_PLAYERS} spelers.")

        names = [name.strip() for name, _ in player_details]
        if any(not name for name in names):
            raise ValueError("Elke speler heeft een naam nodig.")
        if len(set(name.casefold() for name in names)) != len(names):
            raise ValueError("Elke speler moet een unieke naam hebben.")

        colors = [color for _, color in player_details]
        if len(set(colors)) != len(colors):
            raise ValueError("Elke speler moet een unieke kleur kiezen.")
