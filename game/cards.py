"""Actiekaarten en kaartstapel voor Treasure Run."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from random import Random


class CardColor(str, Enum):
    """De vijf kleuren die op actiekaarten kunnen voorkomen."""

    BLUE = "Blauw"
    GREEN = "Groen"
    ORANGE = "Oranje"
    PURPLE = "Paars"
    YELLOW = "Geel"


class CardAction(str, Enum):
    """Een extra actie die een actiekaart kan bevatten."""

    BOAT = "Boot"
    GUARD = "Guards"
    CAMOUFLAGE = "Camouflage"


@dataclass(frozen=True, slots=True)
class ActionCard:
    """Een speelbare kaart met waarde, kleur en nul tot twee acties."""

    value: int
    color: CardColor
    actions: tuple[CardAction, ...] = ()

    @property
    def action_label(self) -> str:
        """Geef de acties als leesbare tekst terug."""
        return " · ".join(action.value for action in self.actions) or "Geen actie"


def create_action_cards() -> list[ActionCard]:
    """Maak de 50 actiekaarten uit de Project Bible.

    De Bible beschrijft 25 unieke kaarten, elk in twee exemplaren.
    """
    patterns: tuple[tuple[int, CardColor, tuple[CardAction, ...]], ...] = (
        (2, CardColor.BLUE, (CardAction.BOAT,)),
        (3, CardColor.GREEN, (CardAction.BOAT, CardAction.BOAT)),
        (4, CardColor.ORANGE, (CardAction.BOAT, CardAction.BOAT)),
        (5, CardColor.PURPLE, (CardAction.BOAT, CardAction.BOAT)),
        (6, CardColor.YELLOW, (CardAction.BOAT, CardAction.BOAT)),
        (2, CardColor.GREEN, (CardAction.BOAT, CardAction.GUARD)),
        (3, CardColor.ORANGE, (CardAction.GUARD, CardAction.GUARD)),
        (4, CardColor.PURPLE, (CardAction.GUARD, CardAction.GUARD)),
        (5, CardColor.YELLOW, (CardAction.GUARD, CardAction.GUARD)),
        (6, CardColor.BLUE, (CardAction.GUARD, CardAction.GUARD)),
        (2, CardColor.ORANGE, (CardAction.GUARD, CardAction.GUARD)),
        (3, CardColor.PURPLE, (CardAction.GUARD, CardAction.GUARD)),
        (4, CardColor.YELLOW, (CardAction.GUARD, CardAction.GUARD)),
        (5, CardColor.BLUE, (CardAction.GUARD, CardAction.GUARD)),
        (6, CardColor.GREEN, (CardAction.GUARD, CardAction.GUARD)),
        (2, CardColor.PURPLE, (CardAction.GUARD, CardAction.CAMOUFLAGE)),
        (3, CardColor.YELLOW, (CardAction.CAMOUFLAGE, CardAction.CAMOUFLAGE)),
        (4, CardColor.BLUE, (CardAction.CAMOUFLAGE, CardAction.CAMOUFLAGE)),
        (5, CardColor.GREEN, (CardAction.CAMOUFLAGE, CardAction.CAMOUFLAGE)),
        (6, CardColor.ORANGE, (CardAction.CAMOUFLAGE, CardAction.CAMOUFLAGE)),
        (2, CardColor.YELLOW, (CardAction.CAMOUFLAGE,)),
        (3, CardColor.BLUE, ()),
        (4, CardColor.GREEN, ()),
        (5, CardColor.ORANGE, ()),
        (6, CardColor.PURPLE, ()),
    )
    return [ActionCard(value, color, actions) for _ in range(2) for value, color, actions in patterns]


@dataclass(slots=True)
class ActionDeck:
    """Beheert de trekstapel en aflegstapel van actiekaarten."""

    draw_pile: list[ActionCard] = field(default_factory=create_action_cards)
    discard_pile: list[ActionCard] = field(default_factory=list)

    def shuffle(self) -> None:
        """Schud de trekstapel met een onafhankelijke willekeurige generator."""
        Random().shuffle(self.draw_pile)

    def draw(self, count: int = 1) -> list[ActionCard]:
        """Trek maximaal ``count`` kaarten uit de trekstapel.

        Args:
            count: Het gevraagde aantal kaarten; dit moet niet-negatief zijn.

        Returns:
            De getrokken kaarten, mogelijk minder dan gevraagd als de stapel leeg is.

        Raises:
            ValueError: Als ``count`` negatief is.
        """
        if count < 0:
            raise ValueError("Het aantal te trekken kaarten kan niet negatief zijn.")
        drawn = self.draw_pile[:count]
        del self.draw_pile[:count]
        return drawn

    def discard(self, cards: list[ActionCard]) -> None:
        """Leg de opgegeven kaarten op de aflegstapel."""
        self.discard_pile.extend(cards)
