# sortVisual.py
import random, pygame

# Window Variables
w, h = 800, 480
fps = 30
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Visual Sorting Algorithms")
clock = pygame.time.Clock()


class Main:
    """
    Handles visual part of the program
    """
    def __init__(self):
        self.running = True

        self.algorithm = None

        # Colours
        self.white = (255, 255, 255)

        self.light_grey = (145, 145, 145)
        self.grey = (100, 100, 100)
        self.dark_grey = (40, 40, 40)

        self.black = (0, 0, 0)

    def drawLines(self):
        """
        Draws lines with heights corresponding to a random number
        :return: None
        """

    def draw(self):
        """
        Draws graphics to the screen, updates the screen
        :return: None
        """
        screen.fill(self.dark_grey)
        pygame.display.update()
        clock.tick(fps)

    def run(self):
        """
        Main driver of the code, brings everything together
        :return: None
        """

        while self.running:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

        pygame.quit()
