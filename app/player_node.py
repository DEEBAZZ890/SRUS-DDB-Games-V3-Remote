
class PlayerNode:
    def __init__(self, player):
        self._player = player       # creates a usable instance of the player
        self._next_player = None        # remains None, unless a neighbouring node/next player exists
        self._previous_player = None    # remains None, unless a neighbouring node/previous player exists

    @property       # getter for the player object
    def player(self):
        return self._player

    @player.setter      # setter for the player object
    def player(self, value):
        self._player = value

    @property       # getter for next player
    def next_player(self):
        return self._next_player

    @next_player.setter     # setter for the next player
    def next_player(self, node):
        self._next_player = node

    @property      # getter for the previous player
    def previous_player(self):
        return self._previous_player

    @previous_player.setter     # setter for the previous player
    def previous_player(self, node):
        self._previous_player = node

    @property       # provides the functionality for the delete by key method by getting the player uid from player
    def key(self):
        return self._player._uid

    def __str__(self):      # returns a readable string of the player object
        return f"{self.player._uid} - {self.player._name}"



