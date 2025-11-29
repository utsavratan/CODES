import pygame
import random

pygame.init()
screen_width = 300
screen_height = 600
block_size = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

grid_width = screen_width // block_size
grid_height = screen_height // block_size

colors = [
    (0, 0, 0),       # Black (empty)
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Purple
    (0, 255, 255)    # Cyan
]

# Define shapes
shapes = [
    [[1, 1, 1, 1]],             # I
    [[1, 1, 1], [0, 1, 0]],     # T
    [[1, 1], [1, 1]],           # O
    [[0, 1, 1], [1, 1, 0]],     # S
    [[1, 1, 0], [0, 1, 1]],     # Z
    [[1, 1, 1], [1, 0, 0]],     # L
    [[1, 1, 1], [0, 0, 1]]      # J
]

# Define the Tetromino class
class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.randint(1, len(colors) - 1)
        self.x = grid_width // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self):
        for row_idx, row in enumerate(self.shape):
            for col_idx, value in enumerate(row):
                if value:
                    pygame.draw.rect(
                        screen,
                        colors[self.color],
                        pygame.Rect((self.x + col_idx) * block_size, (self.y + row_idx) * block_size, block_size, block_size)
                    )

# Create the grid
def create_grid(locked_positions={}):
    grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
    for y in range(grid_height):
        for x in range(grid_width):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

# Check for collisions
def valid_space(tetromino, grid):
    for row_idx, row in enumerate(tetromino.shape):
        for col_idx, value in enumerate(row):
            if value:
                if (
                    tetromino.x + col_idx < 0 or
                    tetromino.x + col_idx >= grid_width or
                    tetromino.y + row_idx >= grid_height or
                    grid[tetromino.y + row_idx][tetromino.x + col_idx]
                ):
                    return False
    return True

# Clear full lines
def clear_rows(grid, locked_positions):
    cleared_rows = 0
    for y in range(grid_height - 1, -1, -1):
        if 0 not in grid[y]:
            cleared_rows += 1
            # Remove the cleared row and add a new empty row at the top
            del grid[y]
            grid.insert(0, [0 for _ in range(grid_width)])
            # Update locked positions
            for x in range(grid_width):
                if (x, y) in locked_positions:
                    del locked_positions[(x, y)]
    return cleared_rows

# Draw the grid
def draw_grid():
    for y in range(grid_height):
        for x in range(grid_width):
            pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(x * block_size, y * block_size, block_size, block_size), 1)

# Main game loop
def game_loop():
    locked_positions = {}
    grid = create_grid(locked_positions)

    current_tetromino = Tetromino(random.choice(shapes))
    next_tetromino = Tetromino(random.choice(shapes))

    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3
    score = 0

    game_over = False

    while not game_over:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # Tetromino falling
        if fall_time / 1000 >= fall_speed:
            current_tetromino.y += 1
            if not valid_space(current_tetromino, grid) and current_tetromino.y > 0:
                current_tetromino.y -= 1
                # Lock the piece in the grid
                for row_idx, row in enumerate(current_tetromino.shape):
                    for col_idx, value in enumerate(row):
                        if value:
                            locked_positions[(current_tetromino.x + col_idx, current_tetromino.y + row_idx)] = current_tetromino.color
                # Generate a new tetromino
                current_tetromino = next_tetromino
                next_tetromino = Tetromino(random.choice(shapes))
                # Check if the new tetromino is valid (if not, game over)
                if not valid_space(current_tetromino, grid):
                    game_over = True
            fall_time = 0

        # Handle player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_tetromino.x -= 1
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.x += 1
                if event.key == pygame.K_RIGHT:
                    current_tetromino.x += 1
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.x -= 1
                if event.key == pygame.K_DOWN:
                    current_tetromino.y += 1
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.y -= 1
                if event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.rotate()
                        current_tetromino.rotate()
                        current_tetromino.rotate()

        # Clear full rows
        score += clear_rows(grid, locked_positions)

        # Draw everything
        screen.fill((0, 0, 0))
        draw_grid()
        current_tetromino.draw()

        # Draw locked positions (filled blocks)
        for y in range(grid_height):
            for x in range(grid_width):
                if grid[y][x] != 0:
                    pygame.draw.rect(
                        screen, colors[grid[y][x]],
                        pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                    )

        pygame.display.update()

    pygame.quit()

game_loop()
