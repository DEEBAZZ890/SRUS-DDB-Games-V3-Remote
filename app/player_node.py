from __future__ import annotations
from typing import Optional
from app.player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player  # creates a usable instance of the player
        self._next_player = None  # remains None, unless a neighbouring node/next player exists
        self._previous_player = None  # remains None, unless a neighbouring node/previous player exists

    def __str__(self) -> str:  # returns a readable string of the player object
        return f"{self.player._uid} - {self.player._name}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(player={self.player!r})'

    @property  # getter for the player object
    def player(self) -> Player:
        return self._player

    @property  # getter for next player
    def next_player(self) -> Optional[PlayerNode]:
        return self._next_player

    @property  # getter for the previous player
    def previous_player(self) -> Optional[PlayerNode]:
        return self._previous_player

    @property  # provides the functionality for the delete by key method by getting the player uid from player
    def key(self) -> str:
        return self._player._uid

    @player.setter  # setter for the player object
    def player(self, value: Player) -> None:
        self._player = value

    @next_player.setter  # setter for the next player
    def next_player(self, node: Optional[PlayerNode]) -> None:
        self._next_player = node

    @previous_player.setter  # setter for the previous player
    def previous_player(self, node : Optional[PlayerNode]) -> None:
        self._previous_player = node
