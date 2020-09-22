import numpy as np
from EightPuzzleGame_State import State

'''
This class implement one of the Uinformed Search algorithm
You may choose to implement the Breadth-first or Depth-first or Iterative-Deepening search algorithm

'''


class UninformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def check_inclusive(self, s):
        numOpen = 0
        numClosed = 0
        returnValue = [-1, -1]

        # If s is in the open list
        for i in self.openlist:
            if i.equals(s):
                numOpen = 1
                returnValue[1] = self.openlist.index(i)
                break

        # If s is in the closed list
        for i in self.closed:
            if i.equals(s):
                numClosed = 1
                returnValue[1] = self.closed.index(i)
                break

        # If child is not in either list
        if numOpen == 0 and numClosed == 0:
            returnValue[0] = 1
        # If child is already in the open list
        elif numOpen == 1 and numClosed == 0:
            returnValue[0] = 2
        # If child is already in the closed list
        elif numOpen == 1 and numClosed == 1:
            returnValue[0] = 3
        return returnValue


    """
     * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """
    def state_walk(self):
        # add closed state
        self.closed.append(self.current)
        if self.openlist.__contains__(self.current):
            self.openlist.remove(self.current)
        # Move to next state
        walk_state = self.current.tile_seq
        row = 0
        col = 0

        for i in range(len(walk_state)):
            for j in range(len(walk_state[i])):
                if walk_state[i, j] == 0:
                    row = i
                    col = j
                    break

        self.depth += 1

        # Move up blank space
        # Shallow copy of current.tile_seq
        temp = self.current.tile_seq

        if (row - 1) >= 0:
            tiletoswitch = temp[row-1][col]  # The value where the blank tile is in the current state
            temp[row-1][col] = self.current.tile_seq[row][col]  # Moving the blank tile up by placing 0 in row-1
            temp[row][col] = tiletoswitch  # Replacing the spot where the blank tile was with the value right above
            tempState = State(temp, len(temp))  # Creating new temp state from temp array
            check = tempState.state_walk()

            if check == 1:
                # Do Something according to the uninformed search
            elif check == 2:
                # Do something
            elif check == 3:
                # Do something
            else:
                # Something else


        # Move down blank space
        if (row + 1) < len(walk_state):
            temp = self.current.tile_seq[row+1][col]
            self.current.tile_seq[row+1][col] = 0
            self.current.tile_seq[row][col] = temp

        # Move left blank space
        if (col - 1) >= 0:
            temp = self.current.tile_seq[row][col-1]
            self.current.tile_seq[row][col-1] = 0
            self.current.tile_seq[row][col] = temp

        # Move right blank space
        if (col + 1) < len(walk_state):
            temp = self.current.tile_seq[row][col+1]
            self.current.tile_seq[row][col+1] = 0
            self.current.tile_seq[row][col] = temp

    # Check the following to make it work properly
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print( "Current tile_seq = \n" )
            print( self.current.tile_seq )
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
