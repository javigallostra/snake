import numpy

class Snake():

    UP = [-1,0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]

    def __init__(self, snake_id, init_length, init_pos, init_dir):
        
        self._ID = snake_id
        self._body = numpy.zeros([init_length, 2], dtype=int)
        self._dir = self.UP
        
        self.changeDir(init_dir)
        self.__initiatePos(init_pos, init_dir)
        

    def __initiatePos(self, init_pos, init_dir):
        """
        Initiates the coordinates of the body
        """
        self._body[0] = init_pos
        for i in range(1, self._body.shape[0]):
            self._body[i] = self._body[i-1] - self._dir

    def changeDir(self, new_dir):
        """
        Sets the direction
        """
        if new_dir == 'u':
            self._dir = self.UP
        elif new_dir == 'd':
            self._dir = self.DOWN
        elif new_dir == 'l':
            self._dir = self.LEFT
        elif new_dir == 'r':
            self._dir = self.RIGHT

    def move(self, eaten):
        """
        Moves the body according to the direction.
        If eaten, adds a body piece to the end of the snake.
        """
        if eaten:
            self._body = numpy.append(self._body, [self._body[-1]], axis=0)
        for i in range(self._body.shape[0]-1, 0, -1):
            self._body[i] = self._body[i-1]
        self._body[0] += self._dir

    def checkCollision(self, boardSize):
        """
        Returns True if the snake collided with
        itself or the walls.
        Return False if it didn't.
        Boardsize must be [n,n].
        """
        head = self._body[0]
        #Check if any number is outside the walls (right, down)
        if numpy.extract(self._body>=boardSize[0], self._body):
            return True
        #Check if any number is outside the walls (up, left)
        elif numpy.extract(self._body<0, self._body):
            return True
        #Check if head collided with anything
        elif head.tolist() in self._body[1:].tolist():
            return True
        else:
            return False

    def getBody(self):
        return self._body

    def getDir(self):
        return self._dir
        
