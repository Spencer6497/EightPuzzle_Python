import numpy as np
from EightPuzzleGame_State import State

'''
This class implement the Best-First-Search (BFS) algorithm along with the Heuristic search strategies

In this algorithm, an OPEN list is used to store the unexplored states and 
a CLOSE list is used to store the visited state. OPEN list is a priority queue. 
The priority is insured through sorting the OPEN list each time after new states are generated 
and added into the list. The heuristics are used as sorting criteria.

In this informed search, reducing the state space search complexity is the main criterion. 
We define heuristic evaluations to reduce the states that need to be checked every iteration. 
Evaluation function is used to express the quality of informedness of a heuristic algorithm. 

'''


class InformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def sortFun(self, e):
        return e.weight

    """
     * check if the generated state is in open or closed
     * the purpose is to avoid a circle
     * @param s
     * @return
    """

    def check_inclusive(self, s):
        in_open = 0
        in_closed = 0
        ret = [-1, -1]

        for item in self.openlist:
            if item.equals(s):
                in_open = 1
                ret[1] = self.openlist.index(item)
                break

        for item in self.closed:
            if item.equals(s):
                in_closed = 1
                ret[1] = self.closed.index(item)
                break

        if in_open == 0 and in_closed == 0:
            ret[0] = 1  # the child is not in open or closed
        elif in_open == 1 and in_closed == 0:
            ret[0] = 2  # the child is already in open
        elif in_open == 0 and in_closed == 1:
            ret[0] = 3  # the child is already in closed
        return ret

    """
     * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """

    def state_walk(self):
        self.closed.append(self.current)
        self.openlist.remove(self.current)

        walk_state = self.current.tile_seq
        row = 0
        col = 0

        # Get location where the blank tile is
        for i in range(len(walk_state)):
            for j in range(len(walk_state[i])):
                if walk_state[i][j] == 0:
                    row = i
                    col = j
                    break

        self.depth += 1
        """ add closed state
            if len(self.openlist) > 0:
                self.current = self.openlist.pop(0)  # Remove leftmost state from open
    
                # move to the next heuristic state
                walk_state = self.current.tile_seq
                row = 0
                col = 0
    
                # Get location where the blank tile is
                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        if walk_state[i][j] == 0:
                            row = i
                            col = j
                            break
            """
        # Generate children of current based on legal moves
        tempUp = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]
        tempDown = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]
        tempLeft = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]
        tempRight = [[None for j in range(len(walk_state))] for i in range(len(walk_state))]

        ''' The following program is used to do the state space walk '''
        # ↑ move up
        if (row - 1) >= 0:
                for i in range(len(walk_state)):
                    for j in range(len(self.current.tile_seq[i])):
                        tempUp[i][j] = self.current.tile_seq[i][j]

                tiletoswitch = tempUp[row - 1][col]  # The value where the blank tile is in the current state
                tempUp[row - 1][col] = self.current.tile_seq[row][col]  # Moving the blank tile up by placing 0 in row-1
                tempUp[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempUp, self.current.depth + 1)  # Creating new state from new configuration
                check = self.check_inclusive(s)

                # If child not in open or closed
                if (check[0] == 1):
                    # Assign child heuristic value
                    self.heuristic_test(s)
                    self.openlist.append(s)
                # If child in open
                elif (check[0] == 2):
                    if s.depth < self.openlist[check[1]].depth:
                        self.openlist[check[1]].depth = s.depth
                # If child in closed
                elif (check[0] == 3):
                    if s.depth < self.closed[check[1]].depth:
                        self.openlist.append(self.closed.pop(check[1]))
                """
                    *do the next steps according to flag (check)
                    *if flag = 2 //in the open list
                    *if the child was reached by a shorter path
                    *then give the state on open the shorter path
                    *if flag = 3 //in the closed list
                    *if the child was reached by a shorter path then
                     begin
                    *remove the state from closed;
                    *add the child to open
                    *end;
                """
                # TODO your code end here

            # ↓ move down
        if (row + 1) < len(walk_state):
                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        tempDown[i][j] = walk_state[i][j]

                tiletoswitch = tempDown[row + 1][col]  # The value where the blank tile is in the current state
                tempDown[row + 1][col] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempDown[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempDown, self.current.depth + 1)
                check = self.check_inclusive(s)

                # If child not in open or closed
                if (check[0] == 1):
                    # Assign child heuristic value
                    self.heuristic_test(s)
                    self.openlist.append(s)
                # If child in open
                elif (check[0] == 2):
                    if s.depth < self.openlist[check[1]].depth:
                        self.openlist[check[1]].depth = s.depth
                # If child in closed
                elif (check[0] == 3):
                    if s.depth < self.closed[check[1]].depth:
                        self.openlist.append(self.closed.pop(check[1]))

                """
                 *if flag = 2 //in the open list
                 *if the child was reached by a shorter path
                 *then give the state on open the shorter path
                 *if flag = 3 //in the closed list
                 *if the child was reached by a shorter path then
                 *begin
                 *remove the state from closed;
                 *add the child to open
                 *end;
                """
                # TODO your code end here

            # ← move left
        if (col - 1) >= 0:
                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        tempLeft[i][j] = walk_state[i][j]

                tiletoswitch = tempLeft[row][col - 1]  # The value where the blank tile is in the current state
                tempLeft[row][col - 1] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempLeft[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempLeft, self.current.depth + 1)
                check = self.check_inclusive(s)

                # If child not in open or closed
                if (check[0] == 1):
                    # Assign child heuristic value
                    self.heuristic_test(s)
                    self.openlist.append(s)
                # If child in open
                elif (check[0] == 2):
                    if s.depth < self.openlist[check[1]].depth:
                        self.openlist[check[1]].depth = s.depth
                # If child in closed
                elif (check[0] == 3):
                    if s.depth < self.closed[check[1]].depth:
                        self.openlist.append(self.closed.pop(check[1]))

                """
                 *if flag = 2 //in the open list
                 *if the child was reached by a shorter path
                 *then give the state on open the shorter path
                 *if flag = 3 //in the closed list
                 *if the child was reached by a shorter path then
                 *begin
                 *remove the state from closed;
                 *add the child to open
                 *end;
                """
                # TODO your code end here

            # → move right
        if (col + 1) < len(walk_state):
                for i in range(len(walk_state)):
                    for j in range(len(walk_state[i])):
                        tempRight[i][j] = walk_state[i][j]

                tiletoswitch = tempRight[row][col + 1]  # The value where the blank tile is in the current state
                tempRight[row][col + 1] = self.current.tile_seq[row][col]  # Moving blank tile up by placing 0 in row-1
                tempRight[row][col] = tiletoswitch  # Replacing spot where the blank tile was with the value right above
                s = State(tempRight, self.current.depth + 1)
                check = self.check_inclusive(s)

                # If child not in open or closed
                if (check[0] == 1):
                    # Assign child heuristic value
                    self.heuristic_test(s)
                    self.openlist.append(s)
                    # If child in open
                elif (check[0] == 2):
                    if s.depth < self.openlist[check[1]].depth:
                        self.openlist[check[1]].depth = s.depth
                # If child in closed
                elif (check[0] == 3):
                    if s.depth < self.closed[check[1]].depth:
                        self.openlist.append(self.closed.pop(check[1]))
                """
                 *if flag = 2 //in the open list
                 *if the child was reached by a shorter path
                 *then give the state on open the shorter path
                 *if flag = 3 //in the closed list
                 *if the child was reached by a shorter path then
                 *begin
                 *remove the state from closed;
                 *add the child to open
                 *end;
                """
                # TODO your code end here

            # sort the open list first by h(n) then g(n)

        self.openlist.sort(key=self.sortFun)
        self.current = self.openlist[0]


    """
     * Solve the game using heuristic search strategies
     
     * There are three types of heuristic rules:
     * (1) Tiles out of place
     * (2) Sum of distances out of place
     * (3) 2 x the number of direct tile reversals
     
     * evaluation function
     * f(n) = g(n) + h(n)
     * g(n) = depth of path length to start state
     * h(n) = (1) + (2) + (3)
    """

    def heuristic_test(self, current):
        curr_seq = current.tile_seq
        goal_seq = self.goal.tile_seq

        # (1) Tiles out of place
        h1 = 0
        """
         *loop over the curr_seq
         *check the every entry in curr_seq with goal_seq
         
         If a tile is not in it's goal place, sum it to the heuristic estimate.
        """

        for i in range(len(curr_seq)):
            for j in range(len(curr_seq[i])):
                if curr_seq[i][j] != goal_seq[i][j]:
                    h1 += 1

        # (2) Sum of distances out of place
        h2 = 0
        """
         *loop over the goal_seq and curr_seq in nested way
         *locate the entry which has the same value in 
         *curr_seq and goal_seq then calculate the offset
         *through the absolute value of two differences
         *of curr_row-goal_row and curr_col-goal_col
         *absoulte value can be calculated by abs(...)
        """

        for i in range(len(curr_seq)):
            for j in range(len(curr_seq[i])):
                """
                 If a tile is out of place, iterate through the
                 goal state and find where it's supposed to be,
                 then calculate the absolute value of the difference
                 between them and add it to the heuristic score
                """
                if curr_seq[i][j] != goal_seq[i][j]:
                    for k in range(len(goal_seq)):
                        for l in range(len(goal_seq[k])):
                            if curr_seq[i][j] == goal_seq[k][l]:
                                h2 += (abs(i - k) + abs(j - l))

        # (3) 2 x the number of direct tile reversals
        h3 = 0

        for i in range(len(curr_seq)): # Loop row
            for j in range(len(curr_seq[i])): # loop col
                # Check boundary of row
                if (i + 1) < len(curr_seq):
                    # Check element is not 0
                    if curr_seq[i + 1][j] != 0 and curr_seq[i][j] != 0:
                        if curr_seq[i + 1][j] == goal_seq[i][j] and curr_seq[i][j] == goal_seq[i + 1][j]:
                            h3 += 1

                # Check boundary of col
                if (j + 1) < len(curr_seq[i]):
                    # Check element is not 0
                    if curr_seq[i][j + 1] != 0 and curr_seq[i][j] != 0:
                        if curr_seq[i][j + 1] == goal_seq[i][j] and curr_seq[i][j] == goal_seq[i][j + 1]:
                            h3 += 1

        h3 *= 2

        # set the heuristic value for current state
        current.weight = current.depth + h1 + h2 + h3

    # You can choose to print all the states on the search path, or just the start and goal state
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print(np.array(self.current.tile_seq))
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")

