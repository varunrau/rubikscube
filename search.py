class MoveSequence():
	def __init__(self,cube,sequence):
		self.cube = cube
		self.sequence = sequence

	def add_move(self,move):
		self.sequence.append(move)

class Move:
	def __init__(self,name,primed):
		self.name = name
		self.primed = primed

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
