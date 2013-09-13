import csv
import copy
import numpy as np
import random

TOP = 0
LEFT = 1
FRONT = 2
RIGHT =3
BACK = 4
BOTTOM = 5


class Face():
    def __init__(self, listrep):
        self.matrix = np.reshape(listrep,(3,3))
        print self.matrix
	def __init__(self, listrep):
		self.matrix = np.reshape(listrep,(3,3))
		print self.matrix

	def isSolved(self):
		mList = self.matrix.tolist()
		firstElem = mList[0][0]
		for l in mList:
			if l != firstElem:
				return False
		return True
    def isSolved(self):
        mList = self.matrix.tolist()
        firstElem = mList[0][0]
        for l in mList:
            if l != firstElem:
                return False
        return True


class Cube():


class Cube():
    def __init__(self, faces):
	    self.faces = faces
	    self.moves = [self.left, self.right, self.front, self.back, self.bottom, self.top]

    def runMove(self):
    	r = randint()
    	split = 1.0/6
    	curmove = 0
	for move in self.moves:
	    curmove += split
	    if r < curmove:
	    	self.move()



    def left(self, d=False):
	front = self.faces[2].matrix
	back = self.faces[4].matrix
	bottom = self.faces[5].matrix
	right = self.faces[3].matrix
	left = self.faces[2].matrix
	top = self.faces[0].matrix

	tempLeft = left
	left = right
	right = tempLeft
	tempBack = back
	back = front
	front = tempBack
	top = np.rot90(top)
	top = np.rot90(top)
	bottom = np.rot90(bottom)
	bottom = np.rot90(bottom)
	self.right(d)

	tempBack = back
	back = front
	front = tempBack

	tempRight = right
	right = left
	left = tempRight

	top = np.rot90(top)
	top = np.rot90(top)
	bottom = np.rot90(bottom)
	bottom = np.rot90(bottom)

    def front(self, d):
	tempFront, front = self.faces[2].matrix
	back, tempBack = self.faces[4].matrix
	bottom, tempBottom  = self.faces[5].matrix
	right, tempRight = self.faces[3].matrix
	left, tempLeft = self.faces[2].matrix
	top, tempTop = self.faces[0].matrix

	right = front
	front = left
	left = back
	back = tempFront
	top = np.rot90(top)
	bottom = np.rot90(bottom)

	self.faces[2].matrix = front
	self.faces[4].matrix = back
	self.faces[5].matrix = bottom
	self.faces[3].matrix = right
	self.faces[2].matrix = left
	self.faces[0].matrix = top

	self.right(d)

	tempFront, front = self.faces[2].matrix
	back, tempBack = self.faces[4].matrix
	bottom, tempBottom  = self.faces[5].matrix
	right, tempRight = self.faces[3].matrix
	left, tempLeft = self.faces[2].matrix
	top, tempTop = self.faces[0].matrix

	front = right
	right = back
	back = left
	left = tempFront
	top = np.rot90(top)
	top = np.rot90(top)
	top = np.rot90(top)
	bottom = np.rot90(bottom)
	bottom = np.rot90(bottom)
	bottom = np.rot90(bottom)

    def back(self, d):
	tempFront, front = self.faces[2].matrix
	back, tempBack = self.faces[4].matrix
	bottom, tempBottom  = self.faces[5].matrix
	right, tempRight = self.faces[3].matrix
	left, tempLeft = self.faces[2].matrix
	top, tempTop = self.faces[0].matrix

	front = right
	right = back
	back = left
	left = tempFront
	top = np.rot90(top)
	top = np.rot90(top)
	top = np.rot90(top)
	bottom = np.rot90(bottom)
	bottom = np.rot90(bottom)
	bottom = np.rot90(bottom)

	self.right(d)

	tempFront, front = self.faces[2].matrix
	back, tempBack = self.faces[4].matrix
	bottom, tempBottom  = self.faces[5].matrix
	right, tempRight = self.faces[3].matrix
	left, tempLeft = self.faces[2].matrix
	top, tempTop = self.faces[0].matrix

	right = front
	front = left
	left = back
	back = tempFront
	top = np.rot90(top)
	bottom = np.rot90(bottom)



    def right(self, d=False):
	print "implement"
	if dir:
	    top = self.faces[0].matrix
	    t1, t2, t3 = top[0, 2], top[1, 2], top[2, 2]
	    front = self.faces[2].matrix
	    back = self.faces[4].matrix
	    bottom = self.faces[5].matrix
	    right = self.faces[3].matrix
	    topTranspose = top.transpose()
	    topTemp = top
	    frontTrans = front.transpose()
	    topTransposeList = topTranspose.tolist()
	    frontTransposeList = frontTrans.tolist()
	    frontTransposeList[2] = topTransposeList[2]
	    top = np.reshape(topTransposeList, (3, 3)).transpose()

	    b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

	    top[0, 2] = back[0, 2]
	    top[1, 2] = back[1, 2]
	    top[2, 2] = back[2, 2]

	    bottom[0, 2] = front[0, 2]
	    bottom[1, 2] = front[1, 2]
	    bottom[2, 2] = front[2, 2]

	    back[0, 2] = bottom[0, 2]
	    back[1, 2] = bottom[1, 2]
	    back[2, 2] = bottom[2, 2]

	    right = np.rot90(right)
	    right = np.rot90(right)
	    right = np.rot90(right)

	    self.faces[0].matrix = top
	    self.faces[2].matrix = front
	    self.faces[4].matrix = back
	    self.faces[5].matrix = bottom
	    self.faces[3].matrix = right

	else:

	    top = self.faces[0].matrix
	    t1, t2, t3 = top[0, 2], top[1, 2], top[2, 2]
	    front = self.faces[2].matrix
	    back = self.faces[4].matrix
	    bottom = self.faces[5].matrix
	    right = self.faces[3].matrix
	    topTranspose = top.transpose()
	    topTemp = top
	    frontTrans = front.transpose()
	    topTransposeList = topTranspose.tolist()
	    frontTransposeList = frontTrans.tolist()
	    topTransposeList[2] = frontTransposeList[2]
	    top = np.reshape(topTransposeList, (3, 3)).transpose()

	    b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

	    back[0, 2] = t1
	    back[1, 2] = t2
	    back[2, 2] = t3

	    front[0, 2] = bottom[0, 2]
	    front[1, 2] = bottom[1, 2]
	    front[2, 2] = bottom[2, 2]

	    bottom[0, 2] = b1
	    bottom[1, 2] = b2
	    bottom[2, 2] = b3

	    right = np.rot90(right)

	    self.faces[0].matrix = top
	    self.faces[2].matrix = front
	    self.faces[4].matrix = back
	    self.faces[5].matrix = bottom
	    self.faces[3].matrix = right
	    import ipdb; ipdb.set_trace() # BREAKPOINT






    def right(self, d=False):
	    print "implement"
	    if dir:
		top = self.faces[0].matrix
		t1, t2, t3 = top[0, 2], top[1, 2], top[2, 2]
		front = self.faces[2].matrix
		back = self.faces[4].matrix
		bottom = self.faces[5].matrix
		right = self.faces[3].matrix
		topTranspose = top.transpose()
		topTemp = top
		frontTrans = front.transpose()
		topTransposeList = topTranspose.tolist()
		frontTransposeList = frontTrans.tolist()
		frontTransposeList[2] = topTransposeList[2]
		top = np.reshape(topTransposeList, (3, 3)).transpose()

		b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

		top[0, 2] = back[0, 2]
		top[1, 2] = back[1, 2]
		top[2, 2] = back[2, 2]

		bottom[0, 2] = front[0, 2]
		bottom[1, 2] = front[1, 2]
		bottom[2, 2] = front[2, 2]

		back[0, 2] = bottom[0, 2]
		back[1, 2] = bottom[1, 2]
		back[2, 2] = bottom[2, 2]

		right = np.rot90(right)
		right = np.rot90(right)
		right = np.rot90(right)

		self.faces[0].matrix = top
		self.faces[2].matrix = front
		self.faces[4].matrix = back
		self.faces[5].matrix = bottom
		self.faces[3].matrix = right

	    else:

		top = self.faces[0].matrix
		t1, t2, t3 = top[0, 2], top[1, 2], top[2, 2]
		front = self.faces[2].matrix
		back = self.faces[4].matrix
		bottom = self.faces[5].matrix
		right = self.faces[3].matrix
		topTranspose = top.transpose()
		topTemp = top
		frontTrans = front.transpose()
		topTransposeList = topTranspose.tolist()
		frontTransposeList = frontTrans.tolist()
		topTransposeList[2] = frontTransposeList[2]
		top = np.reshape(topTransposeList, (3, 3)).transpose()

		b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

		back[0, 2] = t1
		back[1, 2] = t2
		back[2, 2] = t3

		front[0, 2] = bottom[0, 2]
		front[1, 2] = bottom[1, 2]
		front[2, 2] = bottom[2, 2]

		bottom[0, 2] = b1
		bottom[1, 2] = b2
		bottom[2, 2] = b3

		right = np.rot90(right)

		self.faces[0].matrix = top
		self.faces[2].matrix = front
		self.faces[4].matrix = back
		self.faces[5].matrix = bottom
		self.faces[3].matrix = right
		import ipdb; ipdb.set_trace() # BREAKPOINT




    def right(self, d=False):
	    if d:
            top = self.faces[0].matrix
            t1, t2, t3 = top[0, 2], top[1, 2], top[2, 2]
            front = self.faces[2].matrix
            back = self.faces[4].matrix
            bottom = self.faces[5].matrix
            right = self.faces[3].matrix
            topTranspose = top.transpose()
            topTemp = top
            frontTrans = front.transpose()
            topTransposeList = topTranspose.tolist()
            frontTransposeList = frontTrans.tolist()
            frontTransposeList[2] = topTransposeList[2]
            top = np.reshape(topTransposeList, (3, 3)).transpose()

            b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

            top[0, 2] = back[0, 2]
            top[1, 2] = back[1, 2]
            top[2, 2] = back[2, 2]

            bottom[0, 2] = front[0, 2]
            bottom[1, 2] = front[1, 2]
            bottom[2, 2] = front[2, 2]

            back[0, 2] = bottom[0, 2]
            back[1, 2] = bottom[1, 2]
            back[2, 2] = bottom[2, 2]

            right = np.rot90(right)
            right = np.rot90(right)
            right = np.rot90(right)

            self.faces[0].matrix = top
            self.faces[2].matrix = front
            self.faces[4].matrix = back
            self.faces[5].matrix = bottom
            self.faces[3].matrix = right

	    else:
            top = self.faces[0].matrix
            t1, t2, t3 = top[0, 2], top[1, 2], top[2, 2]
            front = self.faces[2].matrix
            back = self.faces[4].matrix
            bottom = self.faces[5].matrix
            right = self.faces[3].matrix
            topTranspose = top.transpose()
            topTemp = top
            frontTrans = front.transpose()
            topTransposeList = topTranspose.tolist()
            frontTransposeList = frontTrans.tolist()
            topTransposeList[2] = frontTransposeList[2]
            top = np.reshape(topTransposeList, (3, 3)).transpose()

            b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

            back[0, 2] = t1
            back[1, 2] = t2
            back[2, 2] = t3

            front[0, 2] = bottom[0, 2]
            front[1, 2] = bottom[1, 2]
            front[2, 2] = bottom[2, 2]

            bottom[0, 2] = b1
            bottom[1, 2] = b2
            bottom[2, 2] = b3

            right = np.rot90(right)

            self.faces[0].matrix = top
            self.faces[2].matrix = front
            self.faces[4].matrix = back
            self.faces[5].matrix = bottom
            self.faces[3].matrix = right

    def isSolved(self):
        for face in self.faces:
            if not face.isSolved():
                return False
        return True

    def top(self, d=False):
        front_top = self.faces[FRONT].matrix[0, :]
        right_top = self.faces[RIGHT].matrix[0, :]
        back_top = self.faces[BACK].matrix[0, :]
        left_top = self.faces[LEFT].matrix[0, :]
        if not d:
            self.faces[TOP].matrix = np.rot90(self.faces[TOP].matrix, 3)
            self.faces[FRONT].matrix[0, :] = right_top
            self.faces[RIGHT].matrix[0, :] = back_top
            self.faces[BACK].matrix[0, :] = left_top
            self.faces[LEFT].matrix[0, :] = front_top
            print 'Rotate Top Clockwise'
        else:
            self.faces[TOP].matrix = np.rot90(self.faces[TOP].matrix)
            self.faces[FRONT].matrix[0, :] = left_top
            self.faces[RIGHT].matrix[0, :] = front_top
            self.faces[BACK].matrix[0, :] = right_top
            self.faces[LEFT].matrix[0, :] = back_top
            print 'Rotate Top Counterclockwise'

    def bottom(self, d=False):
        print "implement"

	def front(self, d=False):
		print "implement"

	def back(self, d=False):
		print "implement"


def genRandomCube():

    with open("input.txt", "rb") as csvfile:
	    reader = csv.reader(csvfile, delimiter=",")
	    matrix = np.chararray((3, 3))
	    l = []
	    for row in reader:
		    l.append(Face(row))

	    c = Cube(l)
	    for i in xrange(20):
	    	c.runMove()
	    print c

def bfs(start_cube):
	moves = {'front':getattr(cube,'front'),'back':getattr(cube,'back'),'left':getattr(cube,'left'),'right':getattr(cube,'right'),'top':getattr(cube,'top'),'bottom':getattr(cube,'bottom')]

	blank_seq = MoveSequence(start_cube,[])
	queue = [blank_seq]
	while queue:
		operating_cube = queue.pop(0)
		for name, possible_move in moves.items():
			first_copy = copy.deepcopy(operating_cube)
			first_copy.cube.possible_move()
			first_copy.add_move(Move(name,False))

			queue.append(first_copy)
			if first_copy.cube.isSolved():
				return first_copy

			second_copy = copy.deepcopy(operating_cube)
			second_copy.cube.possible_move(True)
			second_copy.add_move(Move(name,True))

			if second_copy.cube.isSolved():
				return second_copy

			queue.append(second_copy)


def determineMoveSequence(start_cube):
	move_sequence = bfs(start_cube)
	return move_sequence.sequence


with open("input2.txt", "rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	matrix = np.chararray((3, 3))
	l = []
	for row in reader:
		l.append(Face(row))

	c = Cube(l)
