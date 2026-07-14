# Treasure Run – Data Model

## Doel

Dit document beschrijft alle objecten die binnen Treasure Run gebruikt worden.

De GameEngine is eigenaar van de volledige spelstatus.

Objecten bevatten alleen hun eigen gegevens en eenvoudige logica.

---

# GameEngine

## Verantwoordelijkheid

De centrale spelcontroller.

Beheert:

* spelers
* bord
* grotten
* kaartendecks
* boten
* guards
* spelstatus
* rondes
* actieve speler

De GameEngine bevat de spelregels.

---

# Board

## Verantwoordelijkheid

Beschrijft het speelbord.

Bevat:

* padvakken
* verbindingen
* grotten
* havens

Het bord kent geen spelers of spelregels.

---

# Player

## Eigenschappen

* naam
* kleur
* positie
* handkaarten
* gedragen schatten
* eigen boten
* camouflage actief (later)
* gepast deze ronde

## Verantwoordelijkheid

Bevat uitsluitend de gegevens van één speler.

---

# Card

## Eigenschappen

* kleur
* waarde
* actie

## Mogelijke acties

* Boat
* Swords
* Camouflage
* Geen actie

Een kaart kent geen spelregels.

---

# Deck

## Verantwoordelijkheid

Beheert een stapel kaarten.

Ondersteunt:

* schudden
* trekken
* afleggen
* opnieuw vormen indien nodig

---

# Cave

## Eigenschappen

* kleur
* schatten

## Verantwoordelijkheid

Beheert uitsluitend de schatten in één grot.

---

# Treasure

## Eigenschappen

* kleur

Later eventueel:

* waarde
* unieke ID

---

# Boat

## Eigenschappen

* eigenaar
* kleur
* laadcapaciteit
* geladen schatten
* speler aan boord

## Verantwoordelijkheid

Beheert uitsluitend één boot.

---

# BoatDeck

## Verantwoordelijkheid

Beheert:

* spelersboten
* neutrale boten

Levert telkens de volgende boot.

---

# Guard

## Eigenschappen

* type
* positie
* richting
* snelheid

## Types

* Trage guard
* Snelle guard

---

# GuardCard

## Eigenschappen

* guardtype
* aantal stappen per spelersaantal

---

# Round

## Eigenschappen

* nummer
* actieve spelers
* startspeler

---

# Turn

## Eigenschappen

* actieve speler
* resterende actiepunten

---

# Enumeraties

## Color

* Blue
* Green
* Yellow
* Orange
* Purple

---

## CardAction

* None
* Boat
* Swords
* Camouflage

---

## GuardType

* Slow
* Fast

---

# Eigenaarschap

De GameEngine bezit:

* Board
* Deck
* BoatDeck
* Guards
* Players

Board bezit:

* Caves
* Havens

Player bezit:

* Handkaarten
* Schatten
* Boten

Cave bezit:

* Treasure

Boat bezit:

* Geladen schatten
* Eventuele speler

---

# Ontwerpregels

* De GameEngine bevat de spelregels.
* Modellen bevatten alleen data en eenvoudige logica.
* Er is altijd slechts één bron van waarheid voor de spelstatus.
* Objecten communiceren via de GameEngine.
* Vermijd dubbele opslag van dezelfde informatie.

---

# Architectuur

```text
GameEngine
│
├── Board
│   ├── Caves
│   └── Harbors
│
├── Players
│   ├── Cards
│   ├── Treasures
│   └── Boats
│
├── Deck
├── BoatDeck
├── Guards
└── Round
```

---

# Ontwikkelprincipe

Nieuwe functionaliteit wordt altijd toegevoegd aan een bestaand model wanneer dat model er verantwoordelijk voor is.

Maak geen nieuwe manager-, service- of helperklassen tenzij daar een duidelijke noodzaak voor bestaat.

Houd de architectuur eenvoudig, leesbaar en uitbreidbaar.
