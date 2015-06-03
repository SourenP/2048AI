import random

class Board():
	end = False
	board = [[]]
	score = 0

	def __init__(self):
		self.board = [[Tile(-1),Tile(-1),Tile(-1),Tile(-1),Tile(-1),Tile(-1)],
					  [Tile(-1),Tile( 0),Tile( 0),Tile( 0),Tile( 0),Tile(-1)],
					  [Tile(-1),Tile( 0),Tile( 0),Tile( 0),Tile( 0),Tile(-1)],
					  [Tile(-1),Tile( 0),Tile( 0),Tile( 0),Tile( 0),Tile(-1)],
			 	 	  [Tile(-1),Tile( 0),Tile( 0),Tile( 0),Tile( 0),Tile(-1)],
			 	 	  [Tile(-1),Tile(-1),Tile(-1),Tile(-1),Tile(-1),Tile(-1)]]
		self.addTile()
		self.addTile()


	def show(self):
		print
		print "Score: " + str(self.score)
		for r in self.board:
			print "%1s %5s %5s %5s %5s %5s" % (r[0].show(), r[1].show(), r[2].show(),
											   r[3].show(), r[4].show(), r[5].show())
			print
		print 


	def move(self, dir):
		moved = False
		r = range(1, 5)
		c = range(1, 5)
		deltaR = 0
		deltaC = 0
		if   dir == "left" or dir == "a":
			deltaC = -1
			vert = False
		elif dir == "right" or dir == "d":
			deltaC = +1
			r.reverse()
			vert = False
		elif dir == "up" or dir == "w":
			deltaR = -1
			vert = True
		elif dir == "down" or dir == "s":
			deltaR = +1
			c.reverse()
			vert = True
		elif dir == "quit":
			return False
		else:
			print "que?"
			return False

		for i in r:
			for j in c:
				rOffset = 0
				cOffset = 0
				cont = True

				while cont:
					if vert:
						cont, move, points = self.board[j+rOffset][i+cOffset].move(self.board[j+rOffset+deltaR][i+cOffset+deltaC])
						rOffset += deltaR
					else:
						cont, move, points = self.board[i+rOffset][j+cOffset].move(self.board[i+rOffset+deltaR][j+cOffset+deltaC])
						cOffset += deltaC

					self.score += points
					if move: moved = True

		return moved	


	def addTile(self):
		indices = self.getEmpties()
		if len(indices):
			i,j = indices[random.randint(0,len(indices)-1)]

			if random.random() < 0.9: 
				value = 2
			else: 
				value = 4

			self.board[i][j].val = value


	def getEmpties(self):
		indices = []
		for i in range(1,5):
			for j in range(1,5):
				if self.board[i][j].empty():
					indices.append((i,j))
		return indices 

	# DOESNT WORK
	# You lose if you have no possible moves (not if all tiles are full)
	def lost(self):
		if len(self.getEmpties()):
			return False
		else:
			return True

class Tile():
	
	def __init__(self, v):
		self.val = v;
		if v == -1:
			self.edge = True
		else:
			self.edge = False

	def show(self):
		if self.edge:
			return "*"
		elif self.empty():
			return "."
		else:
			return self.val

	def move(self, t):
		if not t.edge and not self.empty():
			if t.empty():
				t.val = self.val
				self.val = 0
				return (True, True, 0)
			elif t.val == self.val:
				t.val *= 2
				self.val = 0
				return (False, True, t.val)
		return (False, False, 0)

	def empty(self):
		if self.val == 0:
			return True 
		else: 
			return False


### RUN ###
if __name__ == '__main__':
	g = Board()
	g.show()
	ans = ""
	while ans != "quit":
		ans = raw_input("Move: ")
		moved = g.move(ans)
		if g.lost(): # needs to be fixed
			print "--------------------------"
			print "Score: " + str(g.score)
			print "Game Over"
			print "--------------------------"
			exit()

		if moved:
			g.addTile()
			g.show()









