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
        if len(self.openlist) > 0:
            self.current = self.openlist.pop(0)  # Remove leftmost state from open

            # Get location where blank tile is
            walk_state = self.current.tile_seq
            row = 0
            col = 0

            for i in range(len(walk_state)):
                for j in range(len(walk_state[i])):
                     if walk_state[i][j] == 0:
                        row = i
                        col = j
                        break

            # Generate children of current
            # Empty lists to hold children when moves are legal
            tempUp = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]
            tempDown = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]
            tempLeft = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]
            tempRight = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]

            # Move up blank space
            if (row - 1) >= 0:
                for i in range(len(walk_state)):
                    for j in range(len(self.current.tile_seq[i])):
                        tempUp[i][j] = self.current.tile_seq[i][j]

                tiletoswitch = tempUp[row - 1][col]  # The value where the blank tile is in the current state
                tempUp[row-1][col] = self.current.tile_seq[row][col]  # Moving the blank tile up by placing 0 in row-1
                tempUp[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempUp)  # Creating new state from new configuration
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if check[0] == 1:
                    self.openlist.append(s)

            # Move down blank space
            if (row + 1) < len(walk_state):

                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        tempDown[i][j] = walk_state[i][j]

                tiletoswitch = tempDown[row + 1][col]  # The value where the blank tile is in the current state
                tempDown[row + 1][col] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempDown[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempDown)
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if check[0] == 1:
                    self.openlist.append(s)

            # Move left blank space
            if (col - 1) >= 0:
                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        tempLeft[i][j] = walk_state[i][j]

                tiletoswitch = tempLeft[row][col - 1]  # The value where the blank tile is in the current state
                tempLeft[row][col - 1] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempLeft[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempLeft)
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if check[0] == 1:
                    self.openlist.append(s)

            # Move right blank space
            if (col + 1) < len(walk_state):
                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        tempRight[i][j] = walk_state[i][j]

                tiletoswitch = tempRight[row][col + 1]  # The value where the blank tile is in the current state
                tempRight[row][col + 1] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempRight[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempRight)
                check = self.check_inclusive(s)

                # If child is neither on open or closed list, append it to the open list
                if check[0] == 1:
                    self.openlist.append(s)

            # add current to closed state list
            self.closed.append(self.current)

    # Check the following to make it work properly
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
