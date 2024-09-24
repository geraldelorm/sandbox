# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from typing import (List)
import collections

def wallAndGates(rooms: List[List[int]]) -> None:
    
    def addNeighbours(row: int, col: int) -> None:
        if (((row, col) not in visited) and (0 <= row < ROWS) and (0 <= col < COLS) and (rooms[row][col] != -1)):
            visited.add((row, col))
            queue.append((row, col))
        return
        
    ROWS, COLS = len(rooms), len(rooms[0])
    queue = collections.deque()
    visited = set()
    
    for row in range(ROWS):
        for col in range(COLS):
            if rooms[row][col] == 0:
                queue.append((row, col))
                visited.add((row, col))
                
    distance = 0
    
    while queue:
        L = len(queue)
        for _ in range(L):
            row, col = queue.popleft()
            rooms[row][col] = distance
            
            addNeighbours(row + 1, col)
            addNeighbours(row - 1, col)
            addNeighbours(row, col - 1)
            addNeighbours(row, col + 1)
            
        distance += 1
        
        
    
    
rooms = [[0,-1],[0,2147483647]]
wallAndGates(rooms)
print(rooms)
assert(rooms == [[0,-1],[0,1]])

rooms2 =  [
[2147483647,-1,0,2147483647],
[2147483647,2147483647,2147483647,-1],
[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]]
wallAndGates(rooms2)
print(rooms2)
assert(rooms2 == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]])

rooms3 = [[-1]]
wallAndGates(rooms3)
print(rooms3)
assert(rooms3 == [[-1]])
