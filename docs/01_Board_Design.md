# Treasure Run – Board Design

## Doel

Dit document beschrijft de vaste structuur van het speelbord.

De GameEngine gebruikt dit document als de enige waarheid voor alle bewegingen op het speelbord.

---

# Centraal pad

Het centrale pad bestaat uit **12 vakken**.

```text
Pad 1
Pad 2
Pad 3
Pad 4
Pad 5
Pad 6
Pad 7
Pad 8
Pad 9
Pad 10
Pad 11
Pad 12
```

Pad 6 en Pad 7 vormen samen de startzone.

---

# Grotten

Er zijn vijf grotten.

Iedere grot heeft een vaste kleur.

| Grot   | Ingang         | Geheime uitgang |
| ------ | -------------- | --------------- |
| Grot 1 | Pad 2          | Pad 3           |
| Grot 2 | Pad 4          | Pad 5           |
| Grot 3 | Pad 6 én Pad 7 | Geen            |
| Grot 4 | Pad 9          | Pad 8           |
| Grot 5 | Pad 11         | Pad 10          |

Opmerking:

* Grot 3 heeft **twee hoofdingangen**.
* Grot 3 heeft **geen geheime uitgang**.

---

# Havens

Er zijn vijf havens.

| Haven   | Bereikbaar vanaf pad |
| ------- | -------------------- |
| Haven 1 | Pad 1                |
| Haven 2 | Pad 5                |
| Haven 3 | Pad 6 en Pad 7       |
| Haven 4 | Pad 8                |
| Haven 5 | Pad 12               |

---

# Startpositie

Alle spelers starten op:

* Pad 6
* of Pad 7

Deze twee vakken vormen samen de startzone.

---

# Beweging

Voor de GameEngine geldt:

* spelers bewegen over het centrale pad;
* meerdere spelers mogen op hetzelfde padvak staan;
* guards gebruiken hetzelfde pad;
* later zullen ook boten en havens aan deze vakken gekoppeld worden.

---

# Ontwerpregels

De GameEngine werkt **niet met schermcoördinaten**.

Alle logica gebruikt uitsluitend:

* padnummers;
* grotverbindingen;
* havenverbindingen.

De gebruikersinterface vertaalt deze later naar de juiste positie op het bord.

---

# Configuratie

De verbindingen tussen pad en grotten worden centraal beheerd.

Bijvoorbeeld:

```python
CAVE_CONNECTIONS = {
    1: {
        "entrances": [2],
        "secret_exit": 3,
    },
    2: {
        "entrances": [4],
        "secret_exit": 5,
    },
    3: {
        "entrances": [6, 7],
        "secret_exit": None,
    },
    4: {
        "entrances": [9],
        "secret_exit": 8,
    },
    5: {
        "entrances": [11],
        "secret_exit": 10,
    },
}
```

Alle toekomstige spelregels (bewegen, guards, schatten, boten en havens) maken gebruik van deze configuratie.

---

# Toekomstige uitbreidingen

In latere sprints worden aan dit bord toegevoegd:

* grotinterieur;
* guardroutes;
* havenlogica;
* boten;
* laadzones;
* ontsnappingsregels.

De structuur van het centrale pad blijft daarbij ongewijzigd.
