"""Streamlit-ingangspunt voor Treasure Run Sprint 1."""

from __future__ import annotations

import streamlit as st

from game.cards import CardAction
from game.constants import MAX_PLAYERS, MIN_PLAYERS, PLAYER_COLOR_HEX
from game.engine import GameEngine
from game.models import PlayerColor


def initialise_session() -> None:
    """Initialiseer de spelengine in de Streamlit-sessie indien nodig."""
    if "game_engine" not in st.session_state:
        st.session_state.game_engine = GameEngine()


def render_player_setup() -> None:
    """Toon het formulier voor spelersnamen en kleuren en start een spel."""
    st.subheader("Spelers instellen")
    player_count = st.selectbox(
        "Aantal spelers", options=range(MIN_PLAYERS, MAX_PLAYERS + 1), index=0
    )

    with st.form("new_game_form"):
        details: list[tuple[str, PlayerColor]] = []
        available_colors = list(PlayerColor)
        for index in range(player_count):
            left, right = st.columns([2, 1])
            name = left.text_input(f"Naam speler {index + 1}", key=f"player_name_{index}")
            color = right.selectbox(
                f"Kleur speler {index + 1}",
                options=available_colors,
                format_func=lambda value: value.value,
                key=f"player_color_{index}",
            )
            details.append((name, color))

        submitted = st.form_submit_button("Nieuw spel starten", type="primary")

    if submitted:
        try:
            st.session_state.game_engine.start_new_game(details)
        except ValueError as error:
            st.error(str(error))
        else:
            st.success("Nieuw spel gestart. Alle pionnen staan op het startvak.")


def render_game_status(engine: GameEngine) -> None:
    """Toon de belangrijkste toestand van een gestart spel."""
    if not engine.state.is_started:
        st.info("Kies 2 tot 5 spelers om Treasure Run te beginnen.")
        return

    st.subheader("Spelstatus")
    st.caption("Sprint 3 — speel een kaart om vooruit te bewegen op het pad.")
    render_board(engine)
    for player in engine.state.players:
        color = PLAYER_COLOR_HEX[player.color.value]
        st.markdown(
            f"<div class='player-card'><span class='token' style='background:{color}'></span>"
            f"<strong>{player.name}</strong><span>Padvak {player.position}</span></div>",
            unsafe_allow_html=True,
        )

    st.subheader("Actiekaarten")
    st.caption(
        f"Trekstapel: {len(engine.action_deck.draw_pile)} kaarten · "
        f"Aflegstapel: {len(engine.action_deck.discard_pile)} kaarten"
    )
    for player in engine.state.players:
        st.markdown(f"#### {player.name}")
        if not player.hand:
            st.caption("Deze speler heeft geen kaarten meer.")
            continue

        columns = st.columns(len(player.hand))
        for card_index, (column, card) in enumerate(zip(columns, player.hand)):
            actions = " ".join(_action_icon(action) for action in card.actions) or "—"
            column.markdown(
                f"<div class='action-card {card.color.value.lower()}'>"
                f"<span class='card-value'>{card.value}</span>"
                f"<span class='card-actions'>{actions}</span>"
                f"<small>{card.action_label}</small></div>",
                unsafe_allow_html=True,
            )
            if column.button(
                f"Speel {card.value}", key=f"play_{player.id}_{card_index}", use_container_width=True
            ):
                engine.play_card(player.id, card_index)
                st.rerun()

    if st.button("Spel opnieuw instellen"):
        engine.reset_game()
        st.rerun()


def _action_icon(action: CardAction) -> str:
    """Geef een compact symbool terug voor een kaartactie."""
    return {
        CardAction.BOAT: "⚓",
        CardAction.GUARD: "⚔️",
        CardAction.CAMOUFLAGE: "🫥",
    }[action]


def render_board(engine: GameEngine) -> None:
    """Toon de twaalf vakken van het pad met de spelers op hun huidige positie."""
    st.subheader("Speelbord")
    for row_start in range(1, engine.board.path_spaces + 1, 6):
        columns = st.columns(6)
        for offset, column in enumerate(columns):
            position = row_start + offset
            players = engine.board.players_at(engine.state.players, position)
            labels = " ".join(player.name[:1].upper() for player in players) or "·"
            column.markdown(
                f"<div class='board-space'><strong>Vak {position}</strong><span>{labels}</span></div>",
                unsafe_allow_html=True,
            )


def main() -> None:
    """Start de Streamlit-gebruikersinterface."""
    st.set_page_config(page_title="Treasure Run", page_icon="🗺️", layout="centered")
    st.markdown(
        """<style>
        .player-card {display:flex;align-items:center;gap:.75rem;padding:.8rem 1rem;margin:.5rem 0;
        border:1px solid #e5e7eb;border-radius:.65rem;background:#fff;}
        .player-card span:last-child {margin-left:auto;color:#6b7280;}
        .token {width:1.1rem;height:1.1rem;border-radius:50%;display:inline-block;box-shadow:inset 0 0 0 2px #fff;}
        .board-space {min-height:4.4rem;padding:.5rem;border:1px solid #d1d5db;border-radius:.55rem;background:#f8fafc;
        display:flex;flex-direction:column;justify-content:space-between;}.board-space span {font-size:1.15rem;color:#1f2937;}
        .action-card {min-height:8.5rem;padding:.65rem;border:2px solid #1f2937;border-radius:.6rem;color:#172033;
        background:#fff;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 2px 5px #0002;}
        .card-value {font-size:2.1rem;font-weight:700;line-height:1;}.card-actions {font-size:1.3rem;}
        .action-card small {color:#4b5563;line-height:1.1;}.blauw {border-top-color:#3498db;}.groen {border-top-color:#27ae60;}
        .oranje {border-top-color:#e67e22;}.paars {border-top-color:#8e44ad;}.geel {border-top-color:#f1c40f;}
        </style>""",
        unsafe_allow_html=True,
    )
    initialise_session()
    st.title("🗺️ Treasure Run")
    st.write("Zet je expeditie klaar en begin samen op het startvak.")
    render_player_setup()
    render_game_status(st.session_state.game_engine)


if __name__ == "__main__":
    main()
