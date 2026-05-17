# Scelte implementative — Brain Shift

## Scoring: 0 punti per risposta errata
Abbiamo scelto di non togliere punti per le risposte sbagliate.
Il punteggio parte da 0 e aumenta solo con le risposte corrette (+10).
Abbiamo scelto così perché volevamo che il giocatore non andasse 
in negativo, rendendo il gioco più accessibile.

## Seed fisso a 42
Abbiamo usato il seed 42 per generare le carte. Questo significa che 
ogni partita ha sempre la stessa sequenza di carte. Lo abbiamo fatto 
perché era richiesto dalla specifica per rendere i test riproducibili.

## Feedback visivo non bloccante
Quando il giocatore risponde, la carta diventa verde o rossa per 150ms.
Abbiamo usato un timer invece di pygame.time.wait() perché wait() 
blocca tutto il gioco, mentre così il loop continua a girare normalmente.

## Istruzioni che scompaiono
Le regole del gioco (TOP/BOTTOM) sono visibili all'inizio.
Scompaiono dopo 10 risposte corrette, come richiesto dalla specifica.
Abbiamo scelto 10 perché ci sembrava un numero ragionevole per 
imparare le regole prima di giocare senza aiuto.

## Separazione logica/pygame
Abbiamo tenuto tutta la logica del gioco separata da pygame.
Questo ci ha permesso di testare rules.py e scoring.py con pytest
senza dover aprire una finestra grafica.