import numpy as np
import collections
from EightPuzzleGame_State import State

'''
This class implement one of the Uinformed Search algorithm
You may choose to implement the Breadth-first or Depth-first or Iterative-Deepening search algorithm

'''

'''
    THIS CODE HAS MIXES OF NUMPY ARRAYS AND PYTHON ARRAYS WHICH ARE STRUCTURALLY DIFFERENT
    THEY MUST BE MODIFIED TO BE ABLE TO USE METHODS IN CLASS STATE
'''

class UninformedSearchSolver:
    current = State()
    goal = State()
    openlist = np.array([])
    closed = np.array([])
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def check_inclusive(self, s):
        isinopen = 0
        isinclosed = 0

        # Var will hold whether state is in open or closed list in position 0 and its index in pos 1
        returnValue = [-1, -1]

        # If s is in the open list
        for i in self.openlist:
            if i.equals(s):
                isinopen = 1
                returnValue[1] = self.openlist.index(i)
                break

        # If s is in the closed list
        for i in self.closed:
            if i.equals(s):
                isinclosed = 1
                returnValue[1] = self.closed.index(i)
                break

        # If child is not in either list
        if isinopen == 0 and isinclosed == 0:
            returnValue[0] = 1
        # If child is already in the open list
        elif isinopen == 1 and isinclosed == 0:
            returnValue[0] = 2
        # If child is already in the closed list
        elif isinopen == 1 and isinclosed == 1:
            returnValue[0] = 3
        return returnValue


    """
     * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """
    def state_walk(self):
        while collections.Counter(self.openlist) != collections.Counter(self.closed):
            # Remove leftmost state from open
            if len(self.openlist) > 0:
                self.current = self.openlist.pop(0)

            if self.current.equals(self.goal):
                return

            # Get location where blank tile is
            walk_state = self.current.tile_seq
            row = 0
            col = 0

            for i in range(len(walk_state)):
                for j in range(len(walk_state[i])):
                    if walk_state[i, j] == 0:
                        row = i
                        col = j
                        break

            # Generate children of current
            # Shallow copy of current.tile_seq to hold children when moves are legal
            tempUp = np.array(self.current.tile_seq)
            tempDown = np.array(self.current.tile_seq)
            tempLeft = np.array(self.current.tile_seq)
            tempRight = np.array(self.current.tile_seq)

            # Move up blank space
            if (row - 1) >= 0:
                tiletoswitch = tempUp[row - 1][col]  # The value where the blank tile is in the current state
                tempUp[row-1][col] = self.current.tile_seq[row][col]  # Moving the blank tile up by placing 0 in row-1
                tempUp[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                # check = self.check_inclusive(tempUp)


                s = State(self.current, tempUp, self.current.depth + 1)  # Creating new state from new configuration
                check = self.check_inclusive(s)


                # If child is neither on open or closed list, append it to the open list
                if 0 <= check[0] < 2:
                    # s = State(self.current, tempUp, self.current.depth + 1)  # Creating new state from new configuration
                    self.openlist.append(s)

            # Move down blank space
            if (row + 1) >= 0:
                tiletoswitch = tempDown[row + 1][col]  # The value where the blank tile is in the current state
                tempDown[row + 1][col] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempDown[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                # check = self.check_inclusive(tempDown)
                s = State(self.current, tempDown, self.current.depth + 1)
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if 0 <= check[0] < 2:
                    # s = State(self.current, tempDown, self.current.depth + 1)
                    self.openlist.append(s)

            # Move left blank space
            if (col - 1) >= 0:
                tiletoswitch = tempLeft[row][col - 1]  # The value where the blank tile is in the current state
                tempLeft[row][col - 1] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempLeft[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                # check = self.check_inclusive(tempLeft)

                s = State(self.current, tempLeft, self.current.depth + 1)
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if 0 <= check[0] < 2:
                    # s = State(self.current, tempLeft, self.current.depth + 1)
                    self.openlist.append(s)

            # Move right blank space
            if (col + 1) >= 0:
                tiletoswitch = tempRight[row][col + 1]  # The value where the blank tile is in the current state
                tempRight[row][col + 1] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempRight[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                # check = self.check_inclusive(tempRight)


                s = State(self.current, tempRight, self.current.depth + 1)
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if 0 <= check[0] < 2:
                    # s = State(self.current, tempRight, self.current.depth + 1)
                    self.openlist.append(s)

            # add closed state
            self.closed.append(self.current)

    # Check the following to make it work properly
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print("Current tile_seq")
            print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
