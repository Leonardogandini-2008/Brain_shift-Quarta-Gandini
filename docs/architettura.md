# Architettura — Brain Shift

## Struttura dei moduli

Il progetto è diviso in due parti principali:

### Logica pura (senza pygame)
- `models.py` — descrive com'è fatta una carta da gioco
- `rules.py` — controlla se il numero è pari e se la lettera è una vocale
- `generator.py` — crea carte casuali usando un seed fisso
- `scoring.py` — calcola il punteggio dopo ogni risposta

### Interfaccia grafica (con pygame)
- `config.py` — colori, dimensioni finestra, tempi di gioco
- `ui.py` — disegna tutto quello che vede il giocatore
- `main.py` — avvia il gioco e gestisce il timer e le risposte

## Regola importante
I file di logica pura non importano mai pygame. 
Questo li rende testabili senza aprire una finestra.

## Macchina a stati
Il gioco ha due stati:

- **PLAYING** — il gioco è in corso, il timer scorre, il giocatore risponde
- **RESULTS** — il tempo è scaduto, si mostra il punteggio finale

Si passa da PLAYING a RESULTS quando i 60 secondi finiscono.
Si torna a PLAYING premendo R nella schermata risultati.