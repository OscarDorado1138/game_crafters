
def main():
    Initial_Position = 4
    Player = 0
    outcome = solve(Initial_Position, Primitive, Generate_Moves, Do_Move, Player)
    remoteness = outcome[1]

    print("Initial Position of " + str(Initial_Position) +" results in a " + str(outcome[0]) + " in " + str(remoteness) +" moves.")



def solve(initial_position, primitive, generate_moves, do_move, current_player):

		global_moves = generate_moves(initial_position)

		remoteness = 0
		loss_t = 0
		win_t = 100

		result = "NULL"

		for move in global_moves:
			min_result = branch(1 - current_player, Do_Move(initial_position, move), remoteness)
			if (min_result[0] == "WIN" and win_t > min_result[1]):
				win_t = min_result[1]
			if (min_result[0] == "LOSS"):
				result = "LOSS"
				if (min_result[1] > loss_t):
					loss_t = min_result[1] 

		if(result == "WIN"):
			remoteness = win_t
		else:
			remoteness = loss_t

		return (result, remoteness)

def branch(current_player, position, remoteness):
	remoteness += 1
	if (Primitive(position, current_player) == "Continue"):
		moves = Generate_Moves(position)
		for move in moves:
			return branch(1 - current_player, Do_Move(position, move), remoteness)
	else:
		return (Primitive(position, current_player), remoteness)


def Primitive(position, current_player):
	if (position == 0):
		if (current_player == 1):
			print("no")
			return "WIN"


		else:
			#print("yes")

			return "LOSS"

	else:
		return "Continue"



def Generate_Moves(position):
	moves = []
	if((position - 2) >= 0):
		moves.append(-2)
	if((position - 1) >= 0):
		moves.append(-1)

	return moves




def Do_Move(Position, move):
	return (Position + move)




if __name__ == "__main__":
    main()

