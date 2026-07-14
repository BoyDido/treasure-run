# Treasure Run – Game Flow

## Doel

Dit document beschrijft de volledige volgorde waarin het spel verloopt.

De GameEngine moet deze volgorde altijd respecteren.

---

# Overzicht

Een spel bestaat uit:

1. Setup
2. Rondes
3. Einde spel
4. Puntentelling

---

# 1. Setup

Bij het starten van een nieuw spel gebeurt het volgende:

## 1.1 Spelers

* Maak alle spelers aan.
* Geef iedere speler:

  * pion
  * kleur
  * verbergscherm
* Plaats alle spelers op de startzone (Pad 6 of Pad 7).

---

## 1.2 Actiekaarten

* Maak het volledige kaartendeck.
* Schud het deck.
* Trek nog geen kaarten voor de spelers.

---

## 1.3 Grotten

Maak de vijf grotten.

Voor iedere grot:

* trek kaarten tot de kleur overeenkomt met de grot;
* gebruik de kaartwaarde als aantal schatten;
* leg alle gebruikte kaarten op de aflegstapel.

---

## 1.4 Boten

Maak de botenstapel volgens de spelregels.

De neutrale boten liggen onderaan de stapel.

Er wordt nog geen boot op het bord geplaatst.

---

## 1.5 Guards

Plaats beide guards op hun startpositie.

Hun beweging wordt pas uitgevoerd op het einde van een ronde.

---

# 2. Begin van een ronde

Voor iedere speler:

* maximaal één kaart bewaren uit de vorige ronde;
* trek vier nieuwe kaarten;
* maximum vijf kaarten in de hand.

De startspeler schuift één speler naar links.

---

# 3. Spelersfase

Spelers spelen om beurt.

Tijdens een beurt kiest een speler:

* één of meerdere kaarten spelen;
* of passen.

Een gespeelde kaart gaat onmiddellijk naar de aflegstapel.

Een speler die past neemt geen verdere beurten meer in deze ronde.

Wanneer alle spelers gepast hebben eindigt de ronde.

---

# 4. Gebruik van kaartwaarde

Eén kaart wordt gebruikt voor haar waarde.

De waarde mag vrij verdeeld worden over:

* bewegen;
* schatten nemen;
* schatten laden;
* pion in boot plaatsen.

Voorbeeld:

Kaartwaarde 5

* 2 stappen bewegen
* 1 schat nemen
* 2 schatten laden

---

# 5. Einde van een ronde

Wanneer alle spelers gepast hebben:

## Stap 1

Beweeg beide guards.

---

## Stap 2

Voer de guardkaart uit.

---

## Stap 3

Verwijder alle camouflage.

---

## Stap 4

Vul lege grotten opnieuw op.

Alleen volledig lege grotten worden opnieuw gevuld.

---

## Stap 5

Start een nieuwe ronde.

---

# 6. Boten

Wanneer een boot volledig geladen is:

* vertrekt de boot onmiddellijk;
* de schatten zijn veilig;
* indien nodig verschijnt onmiddellijk een nieuwe boot.

---

# 7. Ontsnappen

Een speler ontsnapt door:

* zijn pion in een eigen boot te plaatsen.

Wanneer de boot vertrekt:

* verdwijnt de speler uit het spel.

---

# 8. Einde van het spel

Wanneer de laatste neutrale boot verschijnt:

* wordt nog één volledige ronde gespeeld.

Daarna eindigt het spel.

---

# 9. Puntentelling

Na het einde van het spel:

* maak zoveel mogelijk sets;
* bereken bonuspunten;
* speler met de hoogste score wint.

---

# Ontwikkelvolgorde

De GameEngine wordt opgebouwd in onderstaande volgorde.

* Setup
* Bord
* Grotten
* Kaarten
* Beweging
* Actiepunten
* Schatten
* Guards
* Guardkaarten
* Camouflage
* Boten
* Laden
* Ontsnappen
* Puntentelling

Nieuwe functionaliteit wordt pas toegevoegd wanneer de vorige volledig werkt.

De GameEngine volgt altijd deze volgorde.
