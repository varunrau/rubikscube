
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
		self.right()

	def right(self, dir=False):
		print "implement"
		if dir:

			top = self.faces[0].matrix
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
			self.faces[0].matrix = np.reshape(topTransposeList, (3, 3)).transpose()

			b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

			top[2, 0] = back[0, 2]
			top[1, 0] = back[1, 2]
			top[0, 0] = back[2, 2]

			bottom[0, 2] = front[0, 2]
			bottom[1, 2] = front[1, 2]
			bottom[2, 2] = front[2, 2]


			bottom[0, 2] = b1
			bottom[1, 2] = b2
			bottom[2, 2] = b3

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
			self.faces[0].matrix = np.reshape(topTransposeList, (3, 3)).transpose()

			b1, b2, b3 = back[0, 2], back[1, 2], back[2, 2]

			back[0, 2] = top[2, 0]
			back[1, 2] = top[1, 0]
			back[2, 2] = top[0 , 0]

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







#			for t, topRow in enumerate(top):
#				for f, frontRow in enumerate(front):
#					if t != f:
#						continue
#					temp = topRow[-1]
#					topRow[-1] = frontRow[-1]
#					frontRow[-1] = temp





	def isSolved(self):
		for face in self.faces:
			if not face.isSolved():
				return False
		return True


	def left(dir=False):
		print "implement"


	def top(dir=False):
        front_top = self.faces[FRONT][0, :]
        right_top = self.faces[RIGHT][0, :]
        back_top = self.faces[BACK][0, :]
        left_top = self.faces[LEFT][0, :]
        if not dir:
            self.faces[TOP] = np.rot90(self.faces[TOP], 3)
            self.faces[FRONT][0, :] = right_top
            self.faces[RIGHT][0, :] = back_top
            self.faces[BACK][0, :] = left_top
            self.faces[LEFT][0, :] = front_top
            print 'Rotate Top Clockwise'
        else:
            self.faces[TOP] = np.rot90(self.faces[TOP])
            self.faces[FRONT][0, :] = left_top
            self.faces[RIGHT][0, :] = front_top
            self.faces[BACK][0, :] = right_top
            self.faces[LEFT][0, :] = back_top
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







