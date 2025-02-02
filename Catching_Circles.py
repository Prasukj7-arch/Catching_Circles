import cv2
import mediapipe as mp
import pygame
import random

# Initialize Mediapipe for Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Dropping and Catching Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Paddle properties
paddle_width, paddle_height = 150, 20
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - paddle_height - 10

# Ball properties
ball_radius = 15
initial_ball_speed = 5
ball_speed = initial_ball_speed  # Dynamic speed
ball = {"x": random.randint(0, WIDTH - ball_radius), "y": 0}

# Game variables
score = 0
game_over = False
clock = pygame.time.Clock()

# Start webcam for hand tracking
cap = cv2.VideoCapture(0)


def reset_game():
    """Resets the game state for a new round."""
    global ball, score, game_over, ball_speed
    ball = {"x": random.randint(0, WIDTH - ball_radius), "y": 0}
    score = 0
    ball_speed = initial_ball_speed  # Reset speed
    game_over = False


while True:
    while not game_over:
        # Read frame from webcam
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # Flip to match pygame coordinates
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Detect hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                x = hand_landmarks.landmark[9].x  # Index finger base as reference
                paddle_x = int(x * WIDTH) - (paddle_width // 2)  # Map hand movement to paddle

        # Keep paddle within screen boundaries
        paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

        # Clear screen
        screen.fill(WHITE)

        # Draw paddle
        pygame.draw.rect(screen, BLACK, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Update ball position
        ball["y"] += ball_speed

        # Increase speed as score increases
        ball_speed = initial_ball_speed + (score * 0.5)  # Increase speed gradually

        # Check if ball missed (game over)
        if ball["y"] > HEIGHT:
            game_over = True

        # Check collision with paddle
        if paddle_y < ball["y"] + ball_radius < paddle_y + paddle_height and paddle_x < ball["x"] < paddle_x + paddle_width:
            ball["x"] = random.randint(0, WIDTH - ball_radius)  # New ball position
            ball["y"] = 0
            score += 1  # Increase score

        # Draw ball
        pygame.draw.circle(screen, RED, (ball["x"], ball["y"]), ball_radius)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()
        clock.tick(30)

        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Show webcam window (optional)
        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to quit
            game_over = True

    # Game Over Screen
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
    play_again_text = font.render("Press SPACE to Play Again", True, GREEN)
    quit_text = font.render("Press Q to Quit", True, RED)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))
    screen.blit(play_again_text, (WIDTH // 4, HEIGHT // 2))
    screen.blit(quit_text, (WIDTH // 4, HEIGHT // 1.6))
    pygame.display.flip()

    # Wait for user input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()
                cv2.destroyAllWindows()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    waiting = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()
