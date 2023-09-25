from app.player import Player
from app.player_node import PlayerNode
from typing import List, Optional


class PlayerList:
    def __init__(self) -> None:
        self._head = None  # represents the head/first node in the player list
        self._tail = None  # represents the tail/last node in the player list

    @property
    def head(self) -> Optional[PlayerNode]:
        return self._head

    @property
    def tail(self) -> Optional[PlayerNode]:
        return self._tail

    @tail.setter
    def tail(self, new_node: Optional[PlayerNode]) -> None:
        self._tail = new_node

    def __repr__(self) -> str:  # Raf hint for debugging and good practice
        class_name = self.__class__.__name__
        return f'{class_name}(Player Nodes={self.to_list()})'

    def is_empty(self) -> bool:  # used to check if list is empty i.e., contains no head player
        return self._head is None

    def to_list(self) -> List[str]:  # added in raf's class week 4
        my_list = []
        current_player = self._head
        while current_player:
            my_list.append(repr(current_player))
            current_player = current_player.next_player
        return my_list

    def display(self, forward=True) -> None:  # Displays all existing nodes, utilizing the str method of the player node class
        if self.is_empty():
            raise ValueError("Deletion failed. List is empty; No head node exists")
        if forward:
            current = self._head
            while current is not None:
                print(current)
                current = current.next_player
        else:
            current = self._tail
            while current is not None:
                print(current)
                current = current.previous_player

    def insert_head_node(self, player: Player) -> None:
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.next_player = self._head
            self._head.previous_player = new_player
            self._head = new_player

    def insert_tail_node(self, player: Player) -> None:
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.previous_player = self._tail
            self._tail.next_player = new_player
            self._tail = new_player

    def delete_head_node(self) -> None:
        if self.is_empty():
            raise ValueError("Deletion failed. List is empty; No head node exists")
        existing_head = self._head
        self._head = existing_head.next_player
        if self._head is None:
            self._tail = None
        else:
            self._head.previous_player = None

    def delete_tail_node(self) -> None:
        if self._tail is None:
            raise ValueError("Deletion failed. List is empty; No tail node exists")
        else:
            existing_tail = self._tail
            self._tail = existing_tail.previous_player
            if self._tail is None:
                self._head = None
            else:
                self._tail.next_player = None

    def delete_player_node_by_key(self, key: str) -> None:
        player_node = self._head
        while player_node is not None:
            if player_node.key == key:
                deleted_player = player_node.player
                if player_node.previous_player is None:
                    self.delete_head_node()
                elif player_node.next_player is None:
                    self.delete_tail_node()
                else:
                    player_node.previous_player.next_player = player_node.next_player
                    player_node.next_player.previous_player = player_node.previous_player
                return deleted_player
            player_node = player_node.next_player

        raise ValueError(f"Failed to find player with {key} to delete. Deletion not successful")

