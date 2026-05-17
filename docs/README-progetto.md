# Brain Shift — Descrizione del progetto

## Cos'è
Brain Shift è un gioco di reazione rapida sviluppato con Python e pygame.
Ogni round mostra una carta con una lettera e un numero in alto o in basso
sullo schermo. Il giocatore deve rispondere SÌ o NO in base alla posizione.

## Come si gioca
- La carta appare in **alto** → devi rispondere: il numero è pari?
- La carta appare in **basso** → devi rispondere: la lettera è una vocale?
- Freccia destra = SÌ
- Freccia sinistra = NO
- La partita dura 60 secondi
- Risposta corretta: +10 punti

## La difficoltà
Le regole sono semplici, ma la posizione della carta cambia ogni volta
in modo imprevedibile. Non puoi abituarti a una sola risposta: devi
cambiare regola nella testa ad ogni carta.

## Come installarlo
```bash
pip install -r requirements.txt
python main.py
```

## Autori
- Simone Quarta — logica di gioco (rules, models, generator, scoring)
- Leonardo Gandini — interfaccia grafica (config, ui, main)