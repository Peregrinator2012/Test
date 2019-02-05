# -*- coding: utf-8 -*-

from cell_based_forward_search import CellBasedForwardSearch
from queue import PriorityQueue
import math


def heuristics_0(cell, goal):
    """1. Always 0."""
    return 0


def heuristics_constant(cell, goal, c = 1):
    """2. A non-negative constant value c"""
    return c


def heuristics_Euclidean_Distance(cell, goal):
    """3. The Euclidean Distance to the goal."""
    dX = cell.coords[0] - goal.coords[0]
    dY = cell.coords[1] - goal.coords[1]
    L = math.sqrt(dX * dX + dY * dY)
    return L


def heuristics_Octile_Distance(cell, goal):
    """4. The Octile Distance to the goal."""
    dX = abs(cell.coords[0] - goal.coords[0])
    dY = abs(cell.coords[1] - goal.coords[1])
    return dX + dY + (math.sqrt(2) - 2) * min(dX, dY)


def heuristics_Manhattan_Distance(cell, goal):
    """5. The Manhattan Distance to the goal."""
    dX = abs(cell.coords[0] - goal.coords[0])
    dY = abs(cell.coords[1] - goal.coords[1])
    return dX + dY


class AStarPlanner(CellBasedForwardSearch):

    # This implements a simple LIFO (last in first out or depth first) search algorithm

    def __init__(self, title, occupancyGrid):
        CellBasedForwardSearch.__init__(self, title, occupancyGrid)
        self.pq = PriorityQueue()

    # Simply put on the end of the queue
    def pushCellOntoQueue(self, cell):
        h = heuristics_Euclidean_Distance(cell, self.goal)
        if cell.parent == None:
            cell.pathCost = 0
        cell.pathCost += 1
        f = g + h
        self.pq.put((-f, cell))


    # Check the queue size is zero
    def isQueueEmpty(self):
        return not self.pq.empty()

    # Simply pull from the front of the list
    def popCellFromQueue(self):
        cell = self.lifoQueue.pop()
        return cell

    def resolveDuplicate(self, cell, parentCell):
        # Nothing to do in self case
        pass
