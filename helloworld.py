# python helloworld.py
print("Hello world!")

# Variables
game = 'valorant'
print("Game is", game)
print("First letter", game[0])
print("Game string length", len(game))

# Everything in Python is an object; every object has a type

# Strings (type "str")
print("Uppercase game", game.upper())

print(game + " is a good game")

print("Repeating game 10 times", game * 10)

num_games_won = 5
print("I won " + str(num_games_won) + " games in " + game)

print("Using Format: I won {} games in {}".format(num_games_won, game))
print("Using Format: I won {0} games in {1}".format(num_games_won, game))

print("{0:12} | {1:12}".format("Game", "Won"))
print("{0:12} | {1:<12}".format(game, num_games_won))
print("{0:12} | {1:<12}".format("League", 4))
print("{0:12} | {1:<12.2f}".format("CSGO", 2.25))

# Input
input_game = input("Enter a game you like to play: ")
input_games_won = input("Enter how many times you won in this game: ")
print("Input Game:", input_game)
print("Input Games Won:", input_games_won)
