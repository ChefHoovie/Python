class Computer:
    def __init__(NameofGame, game, HardDiskSpace, Graphics, Ram):
        NameofGame.game = game
        NameofGame.HardDiskSpace = HardDiskSpace
        NameofGame.Graphics = Graphics
        NameofGame.Ram = Ram

    def startGame(self, game):
        print("Starting Software:" + game)

Cow = Computer("Tetris", "25MB", "High", "8GB")
print("Type of game: " + Cow.game)
print("Installed space: " + Cow.HardDiskSpace)
print("Graphics set: " + Cow.Graphics)
print("Ram size: " + Cow.Ram)

Cow.startGame("Tetris++")

class laptop(Computer):

    def __init__(NameofGame, game, HardDiskSpace, Graphics, Ram):
     Computer.__init__(NameofGame, game, HardDiskSpace, Graphics, Ram)

Cat = laptop("Puzzle", "16MB", "Low", "12GB")
print("Type of game: " + Cat.game)
print("Installed space: " + Cat.HardDiskSpace)
print("Graphics set: " + Cat.Graphics)
print("Ram size: " + Cat.Ram)

Cat.startGame("Puzzle++")


class desktop(Computer):

    def __init__ (NameofGame, game, HardDiskSpace, Graphics, Ram):
     Computer.__init__(NameofGame, game, HardDiskSpace, Graphics, Ram)

Dog = desktop("JumpingPuzzle", "10MB", "Medium", "2GB")
print("Type of game: " + Dog.game)
print("Installed space: " + Dog.HardDiskSpace)
print("Graphics set: " + Dog.Graphics)
print("Ram size: " + Dog.Ram)

Dog.startGame("JumpingPuzzle++")
