import numpy
from snake import Snake
import random
import time

class Game():

    FOODN = 4
    SNAKEN = 8
    BOARDSIZE = [16, 16]
    STARTINGSIZE = 10
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def __init__(self):
        self.arrayPos = self.__initiatePos()
        self.snake = Snake(self.SNAKEN, self.STARTINGSIZE , [0,11], 'r')
        self.dir = 'r'
        self.food = [1,10]

    def __checkEat(self, headPos):
        """
        Checks for eats.
        Returns True if it ate.
        """
        return bool(headPos.tolist() == self.food)

    def __updateFood(self, board):
        """
        Gives random new coordinates to food from
        the available free spaces in board
        """
        interm = numpy.where(board!=self.SNAKEN, self.arrayPos, board)
        availablePos = numpy.extract(interm!=self.SNAKEN, interm)
        self.food = random.choice(availablePos)
        print("Food now at: " + str(self.food))
        print("Eaten")

    def __prepareBoard(self, eaten):
        """
        Returns a board ready to print
        """
        toprint = numpy.zeros(self.BOARDSIZE, dtype=int)
        bodyPositions = self.snake.getBody()

        #Place snake
        for pos in bodyPositions:
            toprint[pos[0],pos[1]] = self.SNAKEN
        #Replace food
        if eaten:
            self.__updateFood(toprint)
        #Place food
        toprint[self.food[0], self.food[1]] = self.FOODN

        return toprint

    def __initiatePos(self):
        """
        Returns a gameboard-sized array where each
        item contains its position in a python list.
        [[0,0],[0,1]...]
        """
        interm = numpy.empty(self.BOARDSIZE, dtype=object)
        for m in range(interm.shape[0]):
            for n in range(interm.shape[1]):
                interm[m][n] = [m, n]
        
        return interm
        

    def __printBoard(self, board):
        """
        Smoothly prints the game board
        """
        print('')
        
        for line in board:
            lineOut = ''
            for num in line:
                if not num:
                    lineOut += str(num)
                if num==self.FOODN:
                    lineOut += self.OKGREEN + str(num) + self.ENDC
                elif num==self.SNAKEN:
                    lineOut += self.OKBLUE + str(num) + self.ENDC
                lineOut += ' '
            print(lineOut)

        print('')

    def move(self):
        """
        Performs a whole move
        """
        #Update moving direction
        self.snake.changeDir(self.dir)
        #Check for eats in the upcoming move
        futHeadPos = self.snake.getBody()[0] + self.snake.getDir()
        eaten = self.__checkEat(futHeadPos)
        #Move the snake
        self.snake.move(eaten)
        #Check for deads
        if self.snake.checkCollision(self.BOARDSIZE):
            print("PROBLEM")
            return False
        #Or print
        else:
            board = self.__prepareBoard(eaten)
            self.__printBoard(board)
            return True

    def moveTestNTimes(self, times):

        for i in range(times):
            a= str(input())
            if a == 'e':
                break
            self.dir = a
            if not self.move():
                break

        print("\n\n\n TEST ENDED")

    

newGame = Game()
newGame.moveTestNTimes(100)


