#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [Akhil Mokkapati and akmokka]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys
from copy import deepcopy as dc

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
#    board = dc(boar)
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

#reducing space after placing a friend
def reduce_space(rs_boar,row,col):
    rs_board = dc(rs_boar)

    af_board = add_friend(rs_board, row, col)[:]

    lc =max([i for i, value in enumerate(af_board[row][:col+1]) if value == '&' ]+[0])
    uc =af_board[row][col:].index('&')+col if '&' in af_board[row][col:] else len(af_board[row])-1
    for c in range(lc,uc+1):
        if af_board[row][c]=='.':
            af_board[row][c]= 'a'
            
    trans_board = [rt[col] for rt in af_board]
    lr =max([i for i, value in enumerate(trans_board[:row]) if value == '&' ]+[0])
    ur =trans_board[row:].index('&')+row if '&' in trans_board[row:] else len(trans_board)-1
    
    for r in range(lr,ur+1):
       if af_board[r][col]=='.':
            af_board[r][col] ='a'             
    return af_board



# Get list of successors of given board state
def successors(board):
    succ_board = dc(board)
    return [ reduce_space(succ_board, r, c) for r in range(0, len(succ_board)) for c in range(0,len(succ_board[0])) if succ_board[r][c] == '.' ]

# check if board is a goal state
def is_goal(board,k):
    return count_friends(board) == k 

# function to replace 'a' which is introduced to restrict infeasible "."
def replace(solution):
    for r in range(0, len(solution)):
        for c in range(0,len(solution[0])):
            if solution[r][c] == 'a':
               solution[r][c] = '.'
    return solution

#function to transpose board
def Transpose_board(board):
    return list(map(list, zip(*board)))

#function to find maximum F's that can be placed either checking in only rows or columns
def max_possible_k(board):
    max_in_row =len([r for c in board for r in "".join(c).split("&") if len(r)>0 and r not in '#@'])
    max_in_col =len([r for c in Transpose_board(board) for r in "".join(c).split("&") if len(r)>0 and r not in '#@'])
    return max(max_in_row,max_in_col)    

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    test_fringe = [initial_board]
    while len(fringe) >0:
        for s in successors( fringe.pop() ):
            if is_goal(s,K):
                return s
            if s not in test_fringe:
                fringe.append(s)                
                test_fringe.append(s)
    return False


# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    max_k = max_possible_k(IUB_map)
    if K > 0 and K<= max_k:
        solution = solve(IUB_map)
        print ("Here's what we found:")
        print (printable_board(replace(solution)) if solution else "None")
    elif K> max_k:
        print ("Here's what we found:")
        print ("None")
    else:        
        print ("Here's what we found:")
        print (printable_board(IUB_map))



    
    
