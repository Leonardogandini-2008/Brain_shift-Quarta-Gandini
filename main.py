import pygame
import sys
import time
import random

from config import *
from generator import generate_trial, apply_answer
from ui import (
    draw_card,
    draw_hud,
    draw_instructions,
    draw_results
)

def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    rng = random.Random(42)

    trial = generate_trial(rng)

    state = "PLAYING"

    start_time = time.time()

    score = 0
    correct_count = 0
    wrong_count = 0

    feedback_color = None
    feedback_until = 0

    running = True

    while running:

        elapsed = time.time() - start_time

        time_left = GAME_DURATION - elapsed

        if time_left <= 0:
            state = "RESULTS"

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # Restart partita
                if event.key == pygame.K_r:

                    if state == "RESULTS":

                        state = "PLAYING"

                        score = 0
                        correct_count = 0
                        wrong_count = 0

                        rng = random.Random(42)

                        trial = generate_trial(rng)

                        start_time = time.time()

                # Input gioco
                if state == "PLAYING":

                    if event.key == pygame.K_RIGHT:
                        user_answer = True

                    elif event.key == pygame.K_LEFT:
                        user_answer = False

                    else:
                        user_answer = None

                    if user_answer is not None:

                        trial.user_answer = user_answer

                        trial.is_correct = (
                            user_answer == trial.expected_answer
                        )

                        score = apply_answer(
                            score,
                            trial.is_correct
                        )

                        if trial.is_correct:

                            correct_count += 1

                            feedback_color = COLOR_CORRECT

                        else:

                            wrong_count += 1

                            feedback_color = COLOR_WRONG

                        feedback_until = (
                            time.time()
                            + FEEDBACK_MS / 1000
                        )

                        trial = generate_trial(rng)

        screen.fill(COLOR_BG)

        if state == "PLAYING":

            draw_card(
                screen,
                trial,
                feedback_color
                if time.time() < feedback_until
                else None
            )

            draw_hud(
                screen,
                score,
                max(0, time_left),
                correct_count,
                wrong_count
            )

            draw_instructions(
                screen,
                correct_count < INSTRUCTIONS_HIDE_AFTER
            )

        elif state == "RESULTS":

            draw_results(
                screen,
                score,
                correct_count,
                wrong_count
            )

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

    sys.exit()


if __name__ == "__main__":
    main()