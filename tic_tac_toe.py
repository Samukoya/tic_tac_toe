import random
board = [[1,2,3],[4,5,6],[7,8,9]]
def drawBoard(board):
	hor_lines = ['+','-'*9,'+','-'*9,'+','-'*9,'+']
	vert_pieces = ['|',' '*9,'|',' '*9,'|',' '*9,'|']
	for i in board:
		for el in hor_lines:
			print(el, end='')
		print()
		for el2 in vert_pieces:
			print(el2, end='')
		print()
		print('|   ',i[0],'   |   ',i[1],'   |   ',i[2],'   |')
		for el2 in vert_pieces:
			print(el2, end='')
		print()
	for el in hor_lines:
			print(el, end='')
	
def hasWon(board,user):
	if board[0][0] == board[0][1] == board[0][2] == user or board[1][0] == board[1][1] == board[1][2] == user\
	or  board[2][0] == board[2][1] == board[2][2] == user or  board[0][0] == board[1][0] == board[2][0] == user\
	or  board[0][1] == board[1][1] == board[2][1] == user or  board[0][2] == board[1][2] == board[2][2] == user\
	or  board[0][0] == board[1][1] == board[2][2] == user or  board[2][0] == board[1][1] == board[0][2] == user:
		return True
	else:
		return False

def freeFields(board):
	options = []
	for i in board:
		for j in i:
			if type(j)==int:
				options.append(j)
	return options

def comMove(board):
	
	freeMoves = freeFields(board)
	random.shuffle(freeMoves)
	for i in board:
		for j in range(len(i)):
			if i[j] == freeMoves[0]:
				i[j] = 'X'
	
def usrMove(choice,board):
	freeMoves = freeFields(board)
	if choice in freeMoves:
		for i in board:
			for j in range(len(i)):
				if i[j] == choice:
					i[j] = 'O'
	else:
		print("Invalid move")

		
if __name__ == '__main__':
	print("TicTacToe Game")
	while True:
		user = 'O'
		com = 'X'
		comMove(board)
		print("\nCom move:")
		drawBoard(board)
		if hasWon(board, user):
			print("\nPlayer wins!")
			break
		elif hasWon(board, com):
			print("\nComputer wins!")
			break
		elif freeFields(board) == []:
			print("\nTie!")
			break
		print("\nUser move:")
		while True:
			try:
				usr_Move = int(input())
				while(usr_Move not in freeFields(board)):
					print("Invalid move, try again")
					usr_Move = int(input())
				break
			except ValueError:
				print("invalid move, try again")

		usrMove(usr_Move, board)
		drawBoard(board)
		if hasWon(board, user):
			print("\nPlayer wins!")
			break
		elif hasWon(board, com):
			print("\nComputer wins!")
			break
		elif freeFields(board) == []:
			print("\nTie!")
			break
		else:
			continue
