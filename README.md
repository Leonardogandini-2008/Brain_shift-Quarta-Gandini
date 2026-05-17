# Brain Shift

Gioco di rapid task-switching sviluppato con Python e pygame.

## Autori
- Simone Quarta
- Leonardo Gandini

## Installazione
```bash
pip install -r requirements.txt
```

## Avvio
```bash
python main.py
```

## Regole
- La carta appare in alto o in basso
- **TOP**: il numero è pari? → freccia destra SÌ, freccia sinistra NO
- **BOTTOM**: la lettera è una vocale? → freccia destra SÌ, freccia sinistra NO
- La partita dura 60 secondi

## Test
```bash
python -m pytest tests/
```

## Scoring
- Risposta corretta: +10 punti
- Risposta errata: 0 punti

## Struttura del progetto
- `models.py` — descrive com'è fatta una carta (lettera, numero, posizione, risposta)
- `rules.py` — controlla se un numero è pari e se una lettera è una vocale
- `generator.py` — crea carte casuali per ogni turno di gioco
- `scoring.py` — aggiunge i punti quando rispondi correttamente
- `config.py` — contiene i colori, le dimensioni della finestra e i tempi di gioco
- `ui.py` — disegna tutto quello che vedi sullo schermo
- `main.py` — avvia il gioco e gestisce il timer e le risposte del giocatore
- `tests/` — file per verificare che il codice funzioni correttamente