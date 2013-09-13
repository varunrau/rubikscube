import csv
import numpy as np

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

	def isSolved(self):
		mList = self.matrix.tolist()
		firstElem = mList[0][0]
		for l in mList:
			if l != firstElem:
				return False
		return True

class Cube():


    def __init__(self, faces):
	    self.faces = faces

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





    def isSolved(self):
	for face in self.faces:
	    if not face.isSolved():
		return False
	return True


    def left(dir=False):
	print "implement"


    def top(self, dir=False):
        front_top = self.faces[FRONT].matrix[0, :]
        right_top = self.faces[RIGHT].matrix[0, :]
        back_top = self.faces[BACK].matrix[0, :]
        left_top = self.faces[LEFT].matrix[0, :]
        if not dir:
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


    def bottom(dir=False):
        print "implement"

	def front(dir=False):
		print "implement"

	def back(dir=False):
		print "implement"


with open("input2.txt", "rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	matrix = np.chararray((3, 3))
	l = []
	for row in reader:
		l.append(Face(row))

	c = Cube(l)







