'''
Solving Eight Puzzle Game using Search Strategies
The eight-puzzle game is a 3 × 3 version of the 15-puzzle in which eight tiles can be moved around in nine spaces.
CSC 425 525 Artificial Intelligence
Instructor: Dr. Junxiu Zhou
Semester: Fall 2020

Team name: Give Us an A
'''

import numpy as np
import time
from EightPuzzleGame_State import State
from EightPuzzleGame_UinformedSearch import UninformedSearchSolver
from EightPuzzleGame_InformedSearch import InformedSearchSolver

class EightPuzzleGame:
    tiles = 8
    def __init__(self, initial=[], goal=[], tiles=8):
        self.initial = initial
        self.goal = goal
        self.tiles = tiles

    def start(self):
        # initialize the init state and goal state as 2d array
        #init_tile = np.array([[2, 3, 6], [1, 4, 8], [7, 5, 0]])
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])

        # initial state given in prompt for testing
        #init_tile = np.array([[2, 3, 1], [0, 4, 6], [7, 5, 8]])

        init = State(init_tile, 0, 0)

        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        goal = State(goal_tile, 0, 0)

        self.tiles = 8

        print("\nBegin uninformed (Breadth-First) search:")
        UIS_solver = UninformedSearchSolver(init, goal)
        # Time the amount of time it takes to complete computation
        uStartTime = time.time()
        UIS_solver.run()
        uEndTime = time.time()
        uCompTime = uEndTime - uStartTime

        # Print time it took to compute
        print("\n")
        print("Took " + uCompTime.__str__() + " seconds to complete.")

        print("\n")
        print("************************************************************")

        print("\nBegin Informed (Best-First) search:")
        IS_solver = InformedSearchSolver(init, goal)
        # Time computational time
        iStartTime = time.time()
        IS_solver.run()
        iEndTime = time.time()
        iCompTime = iEndTime - iStartTime

        # Print time it took to compute
        print("\n")
        print("Took " + iCompTime.__str__() + " seconds to complete.")

# start the puzzle game
epp = EightPuzzleGame()
epp.start()

