# Part 1: Finding your way

## Goal is to find the shortest path between starting point(🤷‍) and Luddy Hall(🏯) using this map. It is allowed to move one sidewalk square at a time in one of four principal compass directions.


Initial State:
The Starting state of the given map

✔	  ✔	  ✔	  ✔	 🕍	🕍   🕍

✔	 🕍    🕍	 🕍	 ✔	   ✔	   ✔

✔	  ✔	  ✔	 ✔	   🕍	   ✔     ✔	

✔	 🕍     ✔	 🕍	 ✔	   ✔ 	   ✔

✔	 🕍     ✔	 🕍	 ✔	   🕍    ✔

🤷‍♂️  🕍`  ✔    ✔	  ✔	 🕍	 🏯

Goal State:
Reaching the Goal in an optimal pat

✔	  ✔	  ✔	 ✔	 🕍	🕍	   🕍

✔	 🕍	 🕍	🕍	 ✔	   ✔      ✔

🛴	 🛴	🛴	   ✔	 🕍	 ✔    ✔	

🛴	 🕍	🛴	   🕍	 🛴	🛴 	🛴

🛴	 🕍	🛴	   🕍	 🛴	🕍   🛴

🤷‍♂️ 🕍` 🛴    🛴  🛴	🕍	   🏯





## 1.	What is the set of valid states, the successor function, the cost function, the goal state definition, and the initial state?
    *	set of valid states:   All the sidewalks(.) including Luddy Hall (@)
    *	Successor function: Feasible moves (“sidewalks” and “Luddy Hall”) out of 4 possible moves from a point (Horizontal and vertical only).
    *	Cost Function: uniform cost which is length of each move i.e. 1.
    *	Goal State: Reaching Luddy Hall i.e. @
    *	Initial State: Position of # 

## 2.	Why does the program often fail to find a solution? Implement a fix to make the code work better.
    *	In the initial code provided, if there are multiple moves then solution got struck oscillating between precedent and successor step which resulted in an infinite loop. To resolve this, I have implemented a method, to restrict visiting back steps that are already been explored. 
    *	Kept a track of visited steps in a variable “explored” and reduced successor steps that are already visited earlier

## 3.	The existing code is missing a number of the specifications given above. (For example, it doesn't display the path as a string of compass directions.) Complete the implementation, and explain what you did in your report.
    *	I have stored the coordinates of points in the pathway and then by using function “direction_print” derived compass directions using the logic based on the difference of the coordinates for a position with a successor.
    *	If difference  is (1,0) then  ‘N’ , (0,1) then ‘W’ , (-1,0) then ‘S’ and (0,-1) then ‘E’


# Part 2: Hide-and-seek
## Goal is to arrange friends on the IU campus Map such that no two of your friends can see one another.

###### **Initial state**
The starting state of the given map

✔	    ✔	    ✔	   ✔	   🕍	   🕍   🕍

✔	   🕍    🕍	   🕍	   ✔	   ✔	   ✔

✔	    ✔	    ✔	    ✔	   🕍	   ✔     ✔	

✔	   🕍	    ✔	    🕍	✔	   ✔ 	   ✔

✔	   🕍	    ✔	    🕍	✔	   🕍    ✔

🤷‍♂️  🕍`    ✔	  ✔	 ✔	   🕍	   🏯

###### **Goal state**

For K=6 where all the friends are placed without conflicts

🤦‍♂️  ✔	    ✔	    ✔    🕍    🕍   🕍

✔	   🕍	   🕍	   🕍	   ✔	  ✔	  ✔

✔	   ✔	    ✔	   🤦‍♂️ 🕍    ✔     ✔

✔	   🕍	   ✔	   🕍	   ✔	 🤦‍♂️	✔

✔     🕍    🤦‍♂️	 🕍	 ✔	  🕍     🤦‍♂️

🤷‍♂️  🕍`    ✔	 ✔	   🤦‍♂️	🕍	   🏯

## 1.	What is the set of valid states, the successor function, the cost function, the goal state definition, and the initial state?
    *	Set of valid states:   All maps having between 0 to K friends and not more than a friend on the same side of a building or between ## 2 buildings in rows and columns. 
    *	Successor function: Feasible positions for next Friend with not more than a friend on the same side of a building or between 2 buildings in rows and columns. 
    *	Cost Function: Not considering any cost function but restricting infeasible F placements. 
    *	Goal State:  Map with K friends with not more than a friend on the same side of a building or between 2 buildings in rows and columns.
    *	Initial State: Empty map with buildings, luddy hall and My location(#)
## 2. Description of solution:
   *	After adding a new F to the Map , replaced infeasible "." caused due to addition of 'F' by a new character "a". There by restricting the feasible '.' in Successor function for addition of next F's. And also to reduce the solution space, kept track of previously visited states to avoid duplication of visited states. After finding the solution, replaced "a" which was introduced earlier with "." to meet output specifications.
