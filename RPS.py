import random

# Part 1: Implement Player Class
moves = ['rock', 'paper', 'scissors']
class Player: 

   # Set an initial starting score:
   score = 0

   # Create initial method:
   def __init__(self):
       self.my_move = None
       self.their_move = None
    
   #Store the moves of a player: 
   def record(self, my_move, their_move): 
       self.my_move = my_move
       self.their_move = their_move

# Create different subclasses of players: 

     #Asks the user what moves they would like to make: 
class HumanPlayer(Player):
     
     #Create initial method:
    def __init__(self):
        super().__init__()
        self.behavior = 'Primary Player'

     # Create a move method: 
    def move(self): 
        while True: 
            # Get the input of the user through a different set of options
            move = input('please choose rock, paper, or scissors').lower()
            
            # Validate the users input: 
            
            if move in moves: 
                return move
            else: 
                print('Invalid response! Please Try Again.')

    
    # Go through random moves: 
class RandomPlayer(Player):
    def move(self):
        # Return random options of the moves
        return random.choice(moves)

     
class RepeatPlayer(Player):
     def move(self):
         # Play rock
         return 'rock'

     # Remembers what moves the opponent player played during the last round, and would
     # play back that move during the current round
class ReflectPlayer(Player):
    def move(self): 
        #Plays randomly if the other player has not moved
        if self.their_move is None: 
            return random.choice(moves)
        else: 
            # Return the same as the other player
            return self.their_move

     # Remembers what moves it played last round, and cycles through different moves
class CyclePlayer(Player):
     def move(self):
         if self.my_move is None: 
             return random.choice(moves)
         else: 
             index = moves.index(self.my_move) + 1
             if index ==  len(moves):
                 index = 0
             return moves[index]

 
 # Create Options To Win For Both Player 1 and 2: 

 # Player 1: 

     
 
    
    

    

# Part 2: Implement Game Class: 

class Game: 
 
  # Create Initial Methods: 
    def __init__(self, p1, p2):
        
        #Define Players:
        self.p1 = p1
        self.p2 = p2
    
  # Create method for playing rounds:
    def play_round(self):
        # Create Moves:
        move1 = self.p1.move()
        move2 = self.p2.move()
     # Remember the moves of the player for the score: 
        self.p1.record(move1, move2)
        self.p2.record(move1, move2) 

        print(' Here Is The Score: ')
        # Show results: 
        print(f'Player 1: {self.p1.score} | Player 2: {self.p2.score}\n')
       
    def winner(self,one, two):
        self.p_one = one
        self.p_two = two
        victories = {
        one.rock: [two.scissors],  # Rock beats scissors
        one.paper: [two.rock],  # Paper beats rock
        one.scissors: [two.paper]  # Scissors beats paper
    }
        defeats = victories[one]
        if one == two:
            print(f"Both players selected {one}. It's a tie!")
        elif two in defeats:
            print(f"{one} beats {two}! You win!")
            self.p1 +=1
        else:
            print(f"{two} beats {one}! You lose.")
            self.p2 +=1      
       
        
    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round + 1}:")
            self.play_round
            print("Game over!")
            self.p1.score = 0
            self.p2.score = 0
            exit(0)       
    
                

   
        

    
 
    

    


#Initial Main Method: 

if __name__ == '__main__':
    

    behaviors = { 

        'human': HumanPlayer(),
        'reflect': ReflectPlayer(),
        'cycle': CyclePlayer(),
        'random': RandomPlayer(),
        'repeat': RepeatPlayer()

    }

    while True: 
        print('ROCK, PAPER, SCISSORS, GO!\n')
        print('Get Started! Everybody already knows the rules:\n'
              'Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n'
              'Best out of 3 rounds wins!\n'        
        )

        # Let the player choose: 
        choice = input (
            'Choose your Player: (random, reflect, repeat, cycle)\n'
        ).lower()

        # Once the player chooses, the game will start: 
        if choice in behaviors:
            game = Game(behaviors['human'], behaviors[choice])
            game.play_game()
        else:
            print('Wrong player! Please Try Again.')