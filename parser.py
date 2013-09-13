
import csv
import numpy as np

class Face():

	def __init__(self, listrep):
		self.matrix = np.reshape(listrep,(3,3))
		print self.matrix

class Cube()

	def __init__(self, faces):
		self.faces = faces

	def right(dir=False):
		print "implement"
		if dir:
			print "prime"
		else:
			top = self.faces[0]





	def left(dir=False):
		print "implement"

	def top(dir=False):
		print "implement"

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







