from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None       # represents the head/first node in the player list
        self._tail = None       # represents the tail/last node in the player list

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, new_node):
        self._tail = new_node

    def is_empty(self):     # used to check if list is empty i.e., contains no head player
        return self._head is None


    def to_list(self): # added in raf's class week 4
        my_list = []
        current_player = self._head
        while current_player:
            my_list.append(current_player)
            current_player = current_player.next_node
        return my_list

    def __repr__(self) -> str:      # Raf hint for debugging and good practice
        class_name = self.__class__.__name__
        return f'{class_name}(from_list={self.to_list()})'

    def insert_head_node(self, player):     # Inserts a new player as the head. If list is empty, head and tail are updated to reference the newly inserted player
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.next_player = self._head
            self._head.previous_player = new_player
            self._head = new_player
        return new_player

    def delete_head_node(self):     # remove the head of the list. Checks if list is empty. If not, updates references after shifting the nodes
        if self.is_empty():
            return None
        else:
            existing_head = self._head
            self._head = existing_head.next_player
            if self._head is None:
                self._tail = None
            else:
                self._head.previous_player = None
            return existing_head.player

    def insert_tail_node(self, player):     # inserts new player at tail of the list. Checks if no head exists, otherwise adds new player to tail and updates references
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            new_player.previous_player = self._tail
            self._tail.next_player = new_player
            self._tail = new_player
        return new_player

    def delete_tail_node(self):     # Removes the current tail of the list. If the list is empty, returns None. Otherwise checks if the second last entry exists and if found, will promote to the new tail
        if self._tail is None:
            return None
        else:
            existing_tail = self._tail
            self._tail = existing_tail.previous_player
            if self._tail is None:
                self._head = None
            else:
                self._tail.next_player = None
            return existing_tail.player

    def delete_player_node_by_key(self, key):       # deletes a player node by the provided key. Iterates through the list to find the target. Once found, it deletes the node and updates the references of the other nodes
        player_node = self._head
        while player_node is not None:
            if player_node.key == key:
                if player_node.previous_player is None:
                    self.delete_head_node()
                elif player_node.next_player is None:
                    self.delete_tail_node()
                else:
                    player_node.previous_player.next_player = player_node.next_player
                    player_node.next_player.previous_player = player_node.previous_player
                return player_node.player
            player_node = player_node.next_player
        return None

    def display(self, forward=True):        # Displays all existing nodes, utilizing the str method of the player node class
        if self.is_empty():
            print("list is empty")
            return
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
