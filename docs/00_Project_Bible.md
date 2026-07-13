# Treasure Run - Project Bible

**Versie:** 0.1.0
**Status:** In ontwikkeling
**Laatste update:** 12-07-2026

---

# 1. Doel

Deze Project Bible is de officiële referentie voor de ontwikkeling van Treasure Run.

Bij twijfel tussen de code en dit document geldt **dit document**.

We bouwen het spel stap voor stap in kleine sprints. Na elke sprint moet het spel speelbaar blijven.

---

# 2. Projectdoel

Treasure Run wordt ontwikkeld in **Python** met **Streamlit**.

Het doel is om een volledig speelbare digitale versie van het bordspel te maken die lokaal op een pc getest kan worden.

De nadruk ligt op:

* correcte spelregels;
* eenvoudige, leesbare code;
* na elke sprint kunnen testen.

---

# 3. Ontwikkelregels

We volgen altijd dezelfde werkwijze.

1. Beschrijf eerst de sprint.
2. Bouw de sprint.
3. Test de sprint.
4. Los eventuele fouten op.
5. Pas indien nodig deze Project Bible aan.
6. Start de volgende sprint.

Er wordt nooit aan meerdere grote onderdelen tegelijk gewerkt.

---

# 4. Architectuur

De code wordt opgesplitst in twee delen.

## Streamlit

De gebruikersinterface.

Verantwoordelijkheden:

* knoppen tonen;
* spelersinformatie tonen;
* kaarten tonen;
* het spelbord tonen.

## Game Engine

De Game Engine beheert alle spelregels.

Voorbeelden:

* beweging;
* kaarten;
* schatten;
* guards;
* boten;
* score.

---

# 5. Huidige spelstatus

## Sprint 1 – Basis

Status: ✔ Klaar

Opgeleverd:

* Projectstructuur
* Streamlit-app
* Nieuw spel starten
* Spelers toevoegen
* Basis Game Engine

---

## Sprint 2 – Kaarten

Status: ☐ Gepland

Doel:

Een volledig werkend kaartensysteem.

Moet werken:

* deck aanmaken;
* deck schudden;
* kaarten uitdelen;
* hand van iedere speler tonen;
* aflegstapel.

---

# 6. Belangrijke spelregels

Dit hoofdstuk bevat alleen spelregels die definitief zijn.

## Kaarten

* Elke speler krijgt aan het begin van een ronde 4 kaarten.
* Een kaart wordt gebruikt voor **haar waarde** of **haar actie**.
* Nooit beide tegelijk.

*(Aan te vullen tijdens volgende sprints.)*

---

# 7. Belangrijke beslissingen

## 12-07-2026

* We bouwen het spel in kleine sprints.
* Na iedere sprint moet het spel speelbaar blijven.
* Eerst functionaliteit, daarna pas grafische afwerking.
* De Project Bible is de officiële referentie voor de spelregels.

---

# 8. Sprintplanning

| Sprint | Onderwerp          | Status |
| ------ | ------------------ | ------ |
| 1      | Basisproject       | ✔      |
| 2      | Kaarten            | ☐      |
| 3      | Beweging           | ☐      |
| 4      | Schatten           | ☐      |
| 5      | Boten              | ☐      |
| 6      | Guards             | ☐      |
| 7      | Puntentelling      | ☐      |
| 8      | Spel afronden en testen | ☐      |

---

# 9. Werkwijze

Voor elke nieuwe sprint:

* Lees eerst deze Project Bible.
* Bouw alleen de huidige sprint.
* Verander geen bestaande functionaliteit tenzij nodig.
* Zorg dat het spel na de sprint nog opstart met:

```
streamlit run app.py
```

Na het testen wordt deze Project Bible bijgewerkt indien de spelregels of planning gewijzigd zijn.
