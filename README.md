rubikscube
==========

A rubik's cube solver.

How it works

We read in the cube from a csv file and represent the cube as a list of numpy matrices. We wrote a the linear combination for one of the moves (moving the right side of the cube).

To implement the other moves we switched the faces around performed a right operation and switched the faces back. 

To generate random solvable cubes, we started with a solved cube and performed N random moves on the cube.

To solve we performed a naive breadth first search.

Also for funsies we supported rotating the cube.
