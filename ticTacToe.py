#Tic Tac Toe
#By Jozef Komaromy
#2017
#Written in python 3.6

def main():
	def logo():
		print(' ///////////////////////')
		print(' ///       //   //   ///')
		print(' ///       ///      ////')
		print(' ///       //   //   ///')
		print(' ///////////////////////')
		print('TicTacToe by Jozef Komaromy')



	def initBoard():
		board = [[1,2,3],
				 [4,5,6],
				 [7,8,9]]
		return board
	board = initBoard()

	def renderBoard():
		print(board[0][0],'|',board[0][1],'|',board[0][2])
		print('----------')
		print(board[1][0],'|',board[1][1],'|',board[1][2])
		print('----------')
		print(board[2][0],'|',board[2][1],'|',board[2][2])

	def instructions():
		print('Select an unmarked spot!!')
		print('Type a number between 1 and 9 !!')

	def getPos():
		try:
			pos = int(input('Number of your spot :'))
			if pos > 9 or pos < 1:
				getPos()
			elif pos == 1:
				pos = 0,0
			elif pos == 2:
				pos = 0,1
			elif pos == 3:
				pos = 0,2
			elif pos == 4:
				pos = 1,0
			elif pos == 5:
				pos = 1,1
			elif pos == 6:
				pos = 1,2
			elif pos == 7:
				pos = 2,0
			elif pos == 8:
				pos = 2,1
			elif pos == 9:
				pos = 2,2
			return pos
		except:
			getPos()

	def skip():
		for i in range(0,2):
			print('')


	def addX():
		try:
			skip()
			renderBoard()
			print('Its Player 1 (X) turn!')
			instructions()
			try:
				pos = getPos()
			except:
				addX()
			try:
				if board[pos[0]][pos[1]] != 'X' and  board[pos[0]][pos[1]] != 'O':
					board[pos[0]][pos[1]] = 'X'
			except:
				addX()
			winCheck()
		except:
			addX()

	def addO():
		try:
			skip()
			renderBoard()
			print('Its Player 2 (O) turn!')
			instructions()
			try:
				pos = getPos()
			except:
				addO()
			try:
				if board[pos[0]][pos[1]] != 'X' and  board[pos[0]][pos[1]] != 'O':
					board[pos[0]][pos[1]] = 'O'
			except:
				addO()
			winCheck()
		except:
			addO()

	def mainLoop():
		addX()
		addO()
		mainLoop()

	def again():
		renderBoard()
		main()

	def winCheck():
		if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
			print('Player 1 (X) wins!!')
			again()
		elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
			print('Player 1 (X) wins!!')
			again()


		elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
			print('Player 2 (O) wins!!')
			again()
		elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
			print('Player 2 (O) wins!!')
			again()
	logo()
	mainLoop()

main()
