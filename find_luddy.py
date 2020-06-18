#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [Akhil Mokkapati and akmokka]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Find the compass directions of the moves in the solution path.
# solution variable contains sequence of coordinates and cost i.e [(5,0),(4,0),(3,0),3]
def direction_print(solution):
    direction =str(solution[-1])+' ' # Assigning cost  and will append directions in subsequent steps
    for i in range(0,len(solution)-2):
        row_diff = solution[i][0]-solution[i+1][0]
        col_diff = solution[i][1]-solution[i+1][1]
        if row_diff ==1 and col_diff == 0:
            direction+='N'
        elif row_diff ==0 and col_diff == 1:
            direction+='W'
        elif row_diff ==-1 and col_diff == 0:
            direction+='S'
        else:
            direction+='E'
    return direction

# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe=[[you_loc,0]]
    # fringe has elements with each containing path followed to reach the end state in it and cost
    explored =[] 
    while fringe:
        path =fringe.pop(0)   # Queue is used for fringe
        curr_move =path[-2]
        for move in moves(IUB_map, *curr_move):
            if move not in explored:
                new_path = path[:]
                new_path.insert(-1,move) # Adding new postion to the path 
                new_path[-1] = new_path[-1]+1 # incrementing the cost by 1 
                fringe.append(new_path)
                if IUB_map[move[0]][move[1]]=="@":
                    return new_path
        explored.append(curr_move)
         
# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    solution= search1(IUB_map)
    print("Here's the solution I found:")
    if solution:
        direction = direction_print(solution)
        print(direction)
    else: print("Inf")
