"""Unit tests voor de spelengine."""

import unittest

from game.constants import START_POSITION
from game.cards import ActionDeck, CardColor, create_action_cards
from game.engine import GameEngine
from game.models import PlayerColor


class GameEngineTests(unittest.TestCase):
    """Verifieer de setupregels van Sprint 1."""

    def test_start_new_game_places_every_player_on_start(self) -> None:
        """Een nieuw spel start alle spelers op het centrale startvak."""
        engine = GameEngine()

        state = engine.start_new_game(
            [("Ana", PlayerColor.RED), ("Bo", PlayerColor.BLUE)]
        )

        self.assertTrue(state.is_started)
        self.assertEqual([player.position for player in state.players], [START_POSITION] * 2)

    def test_start_new_game_rejects_duplicate_colours(self) -> None:
        """Een kleur mag slechts eenmaal worden gekozen."""
        with self.assertRaisesRegex(ValueError, "unieke kleur"):
            GameEngine().start_new_game(
                [("Ana", PlayerColor.RED), ("Bo", PlayerColor.RED)]
            )

    def test_start_new_game_requires_at_least_two_players(self) -> None:
        """De setup vereist minimaal twee spelers."""
        with self.assertRaisesRegex(ValueError, "tussen 2 en 5"):
            GameEngine().start_new_game([("Ana", PlayerColor.RED)])

    def test_action_deck_contains_fifty_cards_in_two_sets(self) -> None:
        """Het kaartendeck bestaat uit 25 kaarttypes in twee exemplaren."""
        cards = create_action_cards()

        self.assertEqual(len(cards), 50)
        self.assertEqual(sum(card.color is CardColor.BLUE for card in cards), 10)

    def test_start_new_game_shuffles_and_deals_four_cards_per_player(self) -> None:
        """De setup schudt het deck en deelt vier actiekaarten per speler uit."""
        engine = GameEngine()
        state = engine.start_new_game(
            [("Ana", PlayerColor.RED), ("Bo", PlayerColor.BLUE)]
        )

        self.assertEqual([len(player.hand) for player in state.players], [4, 4])
        self.assertEqual(len(engine.action_deck.draw_pile), 42)
        self.assertEqual(engine.action_deck.discard_pile, [])

    def test_discard_adds_cards_to_discard_pile(self) -> None:
        """Afgelegde kaarten blijven beschikbaar in de aflegstapel."""
        deck = ActionDeck()
        cards = deck.draw(2)
        deck.discard(cards)

        self.assertEqual(len(deck.discard_pile), 2)

    def test_play_card_moves_player_and_discards_card(self) -> None:
        """Een gespeelde kaart verplaatst de speler en gaat naar de aflegstapel."""
        engine = GameEngine()
        state = engine.start_new_game(
            [("Ana", PlayerColor.RED), ("Bo", PlayerColor.BLUE)]
        )
        player = state.players[0]
        card = player.hand[0]

        played_card = engine.play_card(player.id, 0)

        self.assertEqual(played_card, card)
        self.assertEqual(player.position, START_POSITION + card.value)
        self.assertEqual(len(player.hand), 3)
        self.assertEqual(engine.action_deck.discard_pile, [card])

    def test_play_card_turns_back_after_last_path_space(self) -> None:
        """Beweging gaat na vak 12 terug naar vak 11."""
        engine = GameEngine()
        state = engine.start_new_game(
            [("Ana", PlayerColor.RED), ("Bo", PlayerColor.BLUE)]
        )
        player = state.players[0]
        player.position = 12
        player.hand[0] = player.hand[0].__class__(2, player.hand[0].color)

        engine.play_card(player.id, 0)

        self.assertEqual(player.position, 10)
        self.assertEqual(player.direction, -1)

    def test_play_card_turns_forward_after_first_path_space(self) -> None:
        """Beweging gaat na vak 1 opnieuw vooruit naar vak 2."""
        engine = GameEngine()
        state = engine.start_new_game(
            [("Ana", PlayerColor.RED), ("Bo", PlayerColor.BLUE)]
        )
        player = state.players[0]
        player.position = 1
        player.direction = -1
        player.hand[0] = player.hand[0].__class__(2, player.hand[0].color)

        engine.play_card(player.id, 0)

        self.assertEqual(player.position, 3)
        self.assertEqual(player.direction, 1)


if __name__ == "__main__":
    unittest.main()
