
def main():
    Initial_Position = 4
    Player = 0
    outcome = solve(Initial_Position, Primitive, Generate_Moves, Do_Move, Player)
    print("Initial Position of " + str(Initial_Position) +" results in a " + str(outcome))



def solve(initial_position, primitive, generate_moves, do_move, current_player):

		global_moves = generate_moves(initial_position)

		result = "LOSS"

		for move in global_moves:
			if (branch(1 - current_player, Do_Move(initial_position, move)) == "LOSS"):
				result = "WIN"
		return result

def branch(current_player, position):
	
	if (Primitive(position, current_player) == "Continue"):

		moves = Generate_Moves(position)
		for move in moves:
			return branch(1 - current_player, Do_Move(position, move))
	else:
		return Primitive(position, current_player)


def Primitive(position, current_player):
	if (position == 0):
		if (current_player == 1):
			return "LOSS"
		else:
			return "WIN"
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

