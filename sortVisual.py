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
        self.scene = 0
        self.val = 1

        # ---- Array Values ---- #
        self.amount = 800
        self.min = 0
        self.max = self.amount + 1

        self.lineWidth = w // self.amount

        self.arr = self.createArr()

        # ---- Algorithms ---- #
        self.qSort = QuickSort(self.arr)
        self.mSort = MergeSort(self.arr)

        self.algorithm = self.mSort

        # ---- Colours ---- #
        self.white = (255, 255, 255)

        self.light_grey = (145, 145, 145)
        self.grey = (100, 100, 100)
        self.dark_grey = (40, 40, 40)

        self.black = (0, 0, 0)

        self.purple = (60, 5, 135)

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

    def drawTitleScene(self):
        """
        Draws the first scene, where user can choose settings
        - amount
        - type of sort
        :return: None
        """
        screen.fill(self.purple)

    def drawSorting(self):
        """
        Draws sorting scene to the screen
        :return: None
        """
        screen.fill(self.dark_grey)
        self.drawLines()

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
            if self.scene == 0:
                self.drawTitleScene()
            elif self.scene == 1:
                self.drawSorting()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    # ---- Sort, then redraw lines ---- #
                    if event.key == pygame.K_RETURN and self.scene == 1:
                        self.arr = self.algorithm.sort()
                        self.drawLines()

                    # ---- Restart Program ---- #
                    if event.key == pygame.K_r:
                        self.reset()  # does not reset the sorting at the moment

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.scene += self.val
                    self.val *= -1

            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
