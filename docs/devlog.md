# Devlog — Brain Shift

## 24 Aprile 2026
- Creato il repository su GitHub
- Rinominato il progetto in Brain_shift Gandini_Quarta

## 13 Maggio 2026
- Leonardo: installata la finestra pygame e scritto il main loop base

## 15 Maggio 2026
- Simone: implementato rules.py con is_even, is_vowel, compute_expected_answer
- Risolto merge conflict tra i due branch

## 16 Maggio 2026
- Simone: implementato models.py con la dataclass Trial
- Simone: implementato generator.py con seed configurabile
- Simone: implementato scoring.py
- Valentino: spostato rules.py nella cartella corretta
- Leonardo: disegnata la carta, aggiunto input tastiera, timer e schermata risultati
- Merge del lavoro dei due membri del team

## 17 Maggio 2026 — Sessione finale
- Aggiunti i file di test del professore in tests/
- Tutti i 27 test passano (python -m pytest tests/)
- Corretti bug di importazione in main.py e rules.py
- Il gioco funziona correttamente
- Aggiunto .gitignore
- Scritto README.md
- Creata documentazione completa in docs/:
  - architettura.md
  - scelte.md
  - uso-ia.md
  - README-progetto.md
  - devlog.md
  - Rimossa cartella __pycache__ dal repository
  - Completata documentazione: architettura, scelte, uso-ia, devlog con bilancio finale
- Aggiunti file di sistema Mac al .gitignore

  ## Bilancio finale

Siamo soddisfatti di essere riusciti a fare un gioco funzionante che rispetta
tutte le specifiche base. La parte più difficile è stata l'integrazione tra
la logica pura e pygame, specialmente correggere gli errori di importazione
e i merge conflict quando lavoravamo in parallelo.

Abbiamo imparato molto su come organizzare un progetto in moduli separati,
su come usare git in coppia senza fare casino, e su come leggere i messaggi
di errore per capire dove stava il problema.

Abbiamo sottovalutato il tempo che avrebbe richiesto la documentazione:
pensavamo di finire il codice in pochi giorni e poi avere molto tempo per
i docs, invece abbiamo dovuto fare tutto di corsa nell'ultima giornata.

La divisione del lavoro è stata abbastanza bilanciata: Simone ha fatto
la logica pura (rules, models, generator, scoring) e Leonardo ha fatto
l'interfaccia grafica (config, ui, main). Ci siamo aiutati quando c'erano
problemi di integrazione.

Se avessimo avuto più tempo avremmo aggiunto il moltiplicatore di punteggio
e il fading graduale delle istruzioni.

Voto che daremmo al nostro progetto: 7/10. Il gioco funziona e rispetta
le specifiche, ma la documentazione è un po' frettolosa e mancano gli
obiettivi avanzati.