import random
import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 512
GRID_WIDTH = 20
GRID_HEIGHT = 16
CELL_WIDTH = SCREEN_WIDTH // GRID_WIDTH
CELL_HEIGHT = SCREEN_HEIGHT // GRID_HEIGHT


def screen_to_grid_point(screen_point: (int, int)) -> (int, int):
    return (int(screen_point[0] / SCREEN_WIDTH * GRID_WIDTH),
            int(screen_point[1] / SCREEN_HEIGHT * GRID_HEIGHT))

def grid_to_screen_point(grid_point: (int, int)) -> (int, int):
    return (int(grid_point[0] / GRID_WIDTH * SCREEN_WIDTH),
            int(grid_point[1] / GRID_HEIGHT * SCREEN_HEIGHT))


class Mole:
    __image: pygame.image
    __pos: (int, int)

    def __init__(self, pos: (int, int)):
        self.__image = pygame.image.load("mole.png")
        self.__pos = pos

    def draw_onto(self, screen: pygame.Surface) -> None:
        screen.blit(self.__image, self.__image.get_rect(topleft=grid_to_screen_point(self.__pos)))

    def get_pos(self) -> (int, int):
        return self.__pos

    def set_pos(self, pos: (int, int)):
        self.__pos = pos


def draw_grid(screen: pygame.Surface) -> None:
    for column in range(GRID_WIDTH):
        pygame.draw.line(screen, "black", (column * CELL_WIDTH, 0), (column * CELL_WIDTH, SCREEN_HEIGHT))

    for row in range(GRID_WIDTH):
        pygame.draw.line(screen, "black", (0, row * CELL_HEIGHT), (SCREEN_WIDTH, row * CELL_HEIGHT))


def __get_rand_grid_position() -> (int, int):
    return (random.randrange(0, GRID_WIDTH),
            random.randrange(0, GRID_HEIGHT))

def get_next_mole_grid_position(current: (int, int)) -> (int, int):
    pos = __get_rand_grid_position()
    while pos == current:
        pos = __get_rand_grid_position()
    return pos


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        mole = Mole((0, 0))

        while running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False
                        break
                    case pygame.MOUSEBUTTONDOWN:
                        if screen_to_grid_point(pygame.mouse.get_pos()) == mole.get_pos():
                            mole.set_pos(get_next_mole_grid_position(mole.get_pos()))

            screen.fill("light green")
            draw_grid(screen)
            mole.draw_onto(screen)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
