# sortVisual.py
import pygame
import random

from mergeSort import MergeSort
from quickSort import QuickSort

# ---- Window Variables ---- #
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

        # ---- Array Values ---- #
        self.amount = 10
        self.min = 0
        self.max = self.amount + 1

        self.lineWidth = w // self.amount

        self.arr = self.createArr()

        # ---- Algorithms ---- #
        self.qSort = QuickSort(self.arr)
        self.mSort = MergeSort()

        self.algorithm = self.qSort

        # ---- Colours ---- #
        self.white = (255, 255, 255)

        self.light_grey = (145, 145, 145)
        self.grey = (100, 100, 100)
        self.dark_grey = (40, 40, 40)

        self.black = (0, 0, 0)

    def createArr(self):
        """
        Creates a list of a certain amount random integers between min and max
        :return arr: arr (python list of integers)
        """
        arr = []

        for i in range(self.amount):
            arr.append(random.randint(self.min, self.max))

        return arr

    def drawLines(self):
        """
        Draws lines with heights corresponding to a random number
        :return: None
        """
        for i in range(self.amount):
            pygame.draw.rect(screen, self.white, (i * self.lineWidth, h - (self.arr[i] * h // self.max),
                                                  self.lineWidth, self.arr[i] * h // self.max))

    def draw(self):
        """
        Draws graphics to the screen, updates the screen
        :return: None
        """
        screen.fill(self.dark_grey)
        self.drawLines()

        pygame.display.update()
        clock.tick(fps)

    def reset(self):
        """
        Resets the array and gui to be sorted again
        :return: None
        """
        self.arr = self.createArr()

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

                    # ---- Sort, then redraw lines ---- #
                    if event.key == pygame.K_RETURN:
                        self.algorithm.sort()
                        self.drawLines()

                    # ---- Restart Program ---- #
                    if event.key == pygame.K_r:
                        self.reset()

        pygame.quit()
