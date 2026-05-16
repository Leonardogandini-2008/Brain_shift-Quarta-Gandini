import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    COLOR_CARD, COLOR_TEXT, COLOR_HUD, COLOR_CORRECT, COLOR_WRONG
)

CARD_WIDTH  = 200
CARD_HEIGHT = 140
CARD_MARGIN = 80   # distanza dal bordo superiore/inferiore

def draw_card(surface, trial, feedback_color=None):
    """Disegna la carta con lettera e numero nella posizione corretta."""
    font_big   = pygame.font.SysFont("Arial", 48, bold=True)
    font_small = pygame.font.SysFont("Arial", 28)

    # Posizione verticale
    if trial.position == "TOP":
        y = CARD_MARGIN
    else:
        y = SCREEN_HEIGHT - CARD_MARGIN - CARD_HEIGHT

    x = (SCREEN_WIDTH - CARD_WIDTH) // 2
    rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

    # Colore carta: feedback se attivo, altrimenti bianco
    color = feedback_color if feedback_color else COLOR_CARD
    pygame.draw.rect(surface, color, rect, border_radius=12)
    pygame.draw.rect(surface, (180, 180, 180), rect, 2, border_radius=12)

    # Lettera
    letter_surf = font_big.render(trial.letter, True, COLOR_TEXT)
    letter_rect = letter_surf.get_rect(center=(x + CARD_WIDTH // 2, y + CARD_HEIGHT // 2 - 15))
    surface.blit(letter_surf, letter_rect)

    # Numero
    number_surf = font_small.render(str(trial.number), True, COLOR_TEXT)
    number_rect = number_surf.get_rect(center=(x + CARD_WIDTH // 2, y + CARD_HEIGHT // 2 + 25))
    surface.blit(number_surf, number_rect)


def draw_hud(surface, score, time_left, correct, wrong):
    """Disegna punteggio, timer e contatori."""
    font = pygame.font.SysFont("Arial", 24)

    score_surf = font.render(f"Score: {score}", True, COLOR_HUD)
    surface.blit(score_surf, (20, 20))

    timer_surf = font.render(f"⏱ {int(time_left)}s", True, COLOR_HUD)
    surface.blit(timer_surf, (SCREEN_WIDTH // 2 - timer_surf.get_width() // 2, 20))

    stats_surf = font.render(f"✓{correct}  ✗{wrong}", True, COLOR_HUD)
    surface.blit(stats_surf, (SCREEN_WIDTH - stats_surf.get_width() - 20, 20))


def draw_instructions(surface, show):
    """Mostra le due regole finché show=True."""
    if not show:
        return
    font = pygame.font.SysFont("Arial", 20)
    color = (160, 160, 160)
    top_surf  = font.render("⬆  TOP: il numero è PARI?", True, color)
    bot_surf  = font.render("⬇  BOTTOM: la lettera è una VOCALE?", True, color)
    surface.blit(top_surf,  (20, SCREEN_HEIGHT // 2 - 30))
    surface.blit(bot_surf,  (20, SCREEN_HEIGHT // 2 + 10))


def draw_results(surface, score, correct, wrong):
    """Schermata risultati finale."""
    font_title = pygame.font.SysFont("Arial", 52, bold=True)
    font_body  = pygame.font.SysFont("Arial", 30)
    font_small = pygame.font.SysFont("Arial", 22)

    total = correct + wrong
    accuracy = (correct / total * 100) if total > 0 else 0

    cx = SCREEN_WIDTH // 2
    lines = [
        (font_title, "RISULTATI",        (255, 220, 60),  130),
        (font_body,  f"Punteggio: {score}",  COLOR_HUD,  210),
        (font_body,  f"Corrette:  {correct}", (80, 200, 120), 260),
        (font_body,  f"Errate:    {wrong}",  (220, 80, 80),  310),
        (font_body,  f"Accuratezza: {accuracy:.1f}%", COLOR_HUD, 360),
        (font_small, "Premi  R  per rigiocare", (140, 140, 140), 450),
    ]
    for font, text, color, y in lines:
        surf = font.render(text, True, color)
        surface.blit(surf, surf.get_rect(center=(cx, y)))