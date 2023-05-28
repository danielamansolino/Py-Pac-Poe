class PyPacPoe():
    board={}
    def __init__(self, turn='X', winner=None, num_wins=1, round_winner={'X': 0, 'O': 0}, ties=0):
        self.board= {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' '
        }
        self.turn = turn 
        self.winner = winner 
        self.num_wins = num_wins 
        self.round_winner = round_winner
        self.ties = ties      

    def print_game(self):
        print('    A   B   C  '  )
        print(f'1)  {self.board["a1"]} | {self.board["b1"]} | {self.board["c1"]} ')  
        print('   -----------')
        print(f'2)  {self.board["a2"]} | {self.board["b2"]} | {self.board["c2"]} ')
        print('   -----------')
        print(f'3)  {self.board["a3"]} | {self.board["b3"]} | {self.board["c3"]} ')
    
    def get_move(self):
        while True:
            player_move = input(f'Player {self.turn}\'s Move (example B2): ').lower()
            if player_move in self.board and self.board[player_move] == ' ':
                return player_move
            else:
                print('Bogus move! Try again...')
    
    def update_board(self, player_move):
        self.board[player_move] = self.turn

    def get_winner(self):
        winning_combinations = [
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # Rows
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # Columns
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']  # Diagonals
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]
        if ' ' not in self.board.values():
            return 'Tie'
        return None
    

    def print_score(self):
        print('SCORE: ')
        print(f'Player X: {self.round_winner["X"]}   Player O: {self.round_winner["O"]}   Ties: {self.ties}')   

    
    def play_game(self):
        print('----------------------')
        print('Let\'s play Py-Pac-Poe!')
        print('----------------------')
        print()

        self.render_num_wins()
        self.print_game()

        while True:
            move = self.get_move()
            self.update_board(move)
            self.print_game()
            winner = self.get_winner()
            if winner:
                if winner == 'Tie':
                    print('Opps! Another tie!')
                    self.ties += 1
                else:
                    print(f'Player {winner} wins the round!')
                    self.round_winner[winner] += 1
                
                self.print_score()

                if self.round_winner['X'] == self.num_wins:
                    print(f'Congrats to player X for winning {self.num_wins} games, Yay!')
                    break
                elif self.round_winner['O'] == self.num_wins:
                    print(f'Congrats to player O for winning {self.num_wins} games, Yay!')
                    break

                self.reset_board()
                self.print_game()
               
            self.turn = 'O' if self.turn == 'X' else 'X'

    def render_num_wins(self):
        while True:
            num_wins = input("Enter the number of wins required: ")
            if num_wins.isdigit():
                self.num_wins = int(num_wins)
                break
            else:
                print("Invalid input. Please enter a valid number.")        

    def reset_board(self):
        self.board = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' '
        }



game = PyPacPoe()
game.play_game()


    