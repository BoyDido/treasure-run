"""Spelcoördinatie voor Treasure Run."""

from __future__ import annotations

from dataclasses import dataclass, field

from .board import Board
from .cards import ActionCard, ActionDeck
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

    def play_card(self, player_id: str, card_index: int) -> ActionCard:
        """Speel een kaart voor beweging en leg deze op de aflegstapel.

        Alleen de waarde van de kaart wordt in Sprint 3 gebruikt. Actiesymbolen
        hebben nog geen speleffect.

        Args:
            player_id: De unieke identificatie van de bewegende speler.
            card_index: De index van de gespeelde kaart in de hand van die speler.

        Returns:
            De gespeelde kaart.

        Raises:
            ValueError: Als het spel niet loopt, de speler niet bestaat of de kaartindex ongeldig is.
        """
        if not self.state.is_started:
            raise ValueError("Start eerst een nieuw spel.")

        player = next((item for item in self.state.players if item.id == player_id), None)
        if player is None:
            raise ValueError("Deze speler bestaat niet in het huidige spel.")
        if not 0 <= card_index < len(player.hand):
            raise ValueError("Kies een kaart uit de hand van deze speler.")

        card = player.hand.pop(card_index)
        player.position, player.direction = self.board.move(
            player.position, player.direction, card.value
        )
        self.action_deck.discard([card])
        return card

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
