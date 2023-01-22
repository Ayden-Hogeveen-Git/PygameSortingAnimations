# sortVisual.py
import pygame
import random

from mergeSort import MergeSort
from quickSort import QuickSort

pygame.init()

# ---- Window Variables ---- #
w, h = 800, 480
fps = 30
icon = pygame.image.load("assets/barsIcon.png")

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Visual Sorting Algorithms")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


class Main:
    """
    Handles visual part of the program
    """
    def __init__(self):
        self.running = True
        self.scene = 0

        # ---- Array Values ---- #
        self.amount = 100
        self.min = 0
        self.max = self.amount - 1
        self.diff = True

        self.lineWidth = w // self.amount

        self.arr = self.createArr()

        # ---- Algorithms ---- #
        self.qSort = QuickSort(self.arr)
        self.mSort = MergeSort(self.arr)

        self.algorithm = self.qSort

        # ---- Colours ---- #
        self.white = (255, 255, 255)

        self.light_grey = (145, 145, 145)
        self.grey = (100, 100, 100)
        self.dark_grey = (40, 40, 40)

        self.black = (0, 0, 0)

        self.red = (200, 10, 10)
        self.purple = (60, 5, 135)

        # ---- Text ---- #
        # Title
        self.titleFont = pygame.font.Font("freesansbold.ttf", 32)

        self.title = self.titleFont.render("Sorting Algorithms", True, self.white)
        self.titleRect = self.title.get_rect()
        self.titleRect.center = (w // 2, h // 10)

        # Start
        self.start = self.titleFont.render("Start", True, self.white)
        self.startRect = self.start.get_rect()
        self.startRect.center = (w // 2, h * 4 // 5)

        # Back
        self.back = self.titleFont.render("back", True, self.white, self.red)
        self.backRect = self.back.get_rect()
        self.backRect.center = (self.backRect.w // 2, self.backRect.h // 2)

    @staticmethod
    def buttonUpdate(button, x, y):
        """
        Checks if the mouse is within the bounds of the button
        :param button: rect object
        :param x: int (location of the mouse on the screen)
        :param y: int (location of the mouse on the screen)
        :return: bool (True if mouse is within the bounds of the button, False otherwise)
        """
        if button.x < x < button.x + button.w \
                and button.y < y < button.y + button.h:
            return True
        return False

    def createArr(self):
        """
        Creates a list of a certain amount random integers between min and max
        :return arr: arr (python list of integers)
        """
        arr = []

        while len(arr) < self.amount:
            val = random.randint(self.min, self.max)
            if not self.diff:
                arr.append(val)
            elif val not in arr:
                arr.append(val)

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
        pygame.draw.line(screen, self.white, (w // 4, h // 7), (w * 3 // 4, h // 7), 2)
        pygame.draw.line(screen, self.white, (w // 4, h * 3 // 4), (w * 3 // 4, h * 3 // 4), 2)
        screen.blit(self.title, self.titleRect)
        screen.blit(self.start, self.startRect)

    def drawSorting(self):
        """
        Draws sorting scene to the screen
        :return: None
        """
        screen.fill(self.dark_grey)
        self.drawLines()
        screen.blit(self.back, self.backRect)

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
                mouseX, mouseY = pygame.mouse.get_pos()

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

                # ---- Mouse Events ---- #
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Start
                    if self.buttonUpdate(self.startRect, mouseX, mouseY) and self.scene == 0:
                        self.scene += 1

                    # Back
                    if self.buttonUpdate(self.backRect, mouseX, mouseY) and self.scene == 1:
                        self.scene -= 1

                # Update Button Colours
                if self.buttonUpdate(self.startRect, mouseX, mouseY):
                    self.start = self.titleFont.render("Start", True, self.red)
                elif self.buttonUpdate(self.backRect, mouseX, mouseY):
                    self.back = self.titleFont.render("Back", True, self.red, self.white)
                else:
                    self.start = self.titleFont.render("Start", True, self.white)
                    self.back = self.titleFont.render("Back", True, self.white, self.red)

            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
