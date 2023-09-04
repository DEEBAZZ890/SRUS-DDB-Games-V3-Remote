import unittest
from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        # Create the player list
        self.test_list = PlayerList()
        # Create the players for testing the player list functionality
        self.player1 = Player("20069321", "Daniel")
        self.player2 = Player("10472204", "John")
        self.player3 = Player("29543305", "Brayden")

    #  Test that inserts a player into an empty list
    def test_insert_head_into_empty_list(self):
        # Check to see if the list is initially empty
        self.assertIsNone(self.test_list._head)
        # Inserts player 1 into the empty list
        self.test_list.insert_head_node(self.player1)
        # Check that player 1 was actually inserted into the player list
        self.assertIs(self.test_list._head.player, self.player1)
        # Check that the next player property of the head is None
        self.assertIsNone(self.test_list._head.next_player)
        # Check that the previous player property of the head is None
        self.assertIsNone(self.test_list._head.previous_player)

    # Test that inserts a player into an already populated list
    def test_insert_head_on_list_with_contents(self):
        # Insert player 1 and make it the head node
        self.test_list.insert_head_node(self.player1)
        # Insert player 2 so that it is takes the place of player 1 as the head node
        self.test_list.insert_head_node(self.player2)
        # Tests that player 2 is now the head node
        self.assertEqual(self.test_list._head.player, self.player2)
        # Check that previous player now points to the previous head - player 1
        self.assertEqual(self.test_list._head.next_player.player, self.player1)
        # Test that previous player is null for the new head
        self.assertIsNone(self.test_list._head.previous_player)
        # Test that the second item in the list has player 2 as the previous_player attribute
        self.assertEqual(self.test_list._head.next_player.previous_player.player, self.player2)

    # Test multiple inserts on the player list and ensure the order of players is preserved when new entries are added
    def test_tail_insert_on_list(self):
        first_tail = self.test_list.insert_tail_node(self.player1)  # Insert the first tail
        second_tail = self.test_list.insert_tail_node(self.player2)  # Insert the second tail
        third_tail = self.test_list.insert_tail_node(self.player3)  # Insert the final/third tail
        # Checks that the first_tail was set to the head as the list was empty
        self.assertIs(self.test_list._head, first_tail)
        # Checks that the most recent tail insert has been correctly set
        self.assertIs(self.test_list._tail, third_tail)
        # Check the player attribute of each node
        self.assertIs(first_tail.player, self.player1)
        self.assertIs(second_tail.player, self.player2)
        self.assertIs(third_tail.player, self.player3)
        # Checks that the second tail is between the head and the tail nodes
        self.assertIs(first_tail.next_player, second_tail)
        # Checks that the second tail's previous attribute points to the head
        self.assertIs(second_tail.previous_player, first_tail)
        # Checks that the second tail's next node points to the new tail
        self.assertIs(second_tail.next_player, third_tail)
        # Checks that the third tail is ordered correctly and points to the second tail as its previous_player
        self.assertIs(third_tail.previous_player, second_tail)

    def test_delete_head_item_from_list(self):   # Tests the delete method when a single entry is stored in the list
        # Test that the delete method returns None when called on an empty list
        self.assertIsNone(self.test_list.delete_head_node())
        # Insert a single player as the head node
        self.test_list.insert_head_node(self.player1)
        # Delete the head node and store the returned player object in deleted_head
        deleted_head = self.test_list.delete_head_node()
        # Check that the deleted_head is the same as the player initially inserted
        self.assertIs(deleted_head, self.player1)
        # Check that the list head is now None, indicating the list is empty
        self.assertIsNone(self.test_list._head)
        # Additionally, verify that the list tail is also None, since the list should be empty
        self.assertIsNone(self.test_list._tail)

    # Tests the delete method on a populated list to ensure that order is preserved when existing items are removed.
    def test_delete_head_method_on_three_player_list(self):
        # Inserts the players from 3rd to first so that Player 1 is the Head after the inserts
        self.test_list.insert_head_node(self.player3)
        self.test_list.insert_head_node(self.player2)
        self.test_list.insert_head_node(self.player1)

        # Store the deleted head node
        deleted_head = self.test_list.delete_head_node()
        # Check that player 1 was successfully deleted
        self.assertIs(deleted_head, self.player1)
        # Check that player 2 is now the new head node
        self.assertIs(self.test_list._head.player, self.player2)
        # Delete the second player/head node
        deleted_head = self.test_list.delete_head_node()
        # Check if the second player was removed as the head node
        self.assertIs(deleted_head, self.player2)
        # Check that player 3 is now the head node
        self.assertIs(self.test_list._head.player, self.player3)
        # Delete the head node
        deleted_head = self.test_list.delete_head_node()
        # Check that the item deleted was in fact player 3
        self.assertIs(deleted_head, self.player3)

        # Final checks to ensure the list is now empty
        # Check if the head attribute returns None/is None
        self.assertIsNone(self.test_list._head)
        # Check if the tail is also None as this means the list is completely empty as intended
        self.assertIsNone(self.test_list._tail)

    # Check that delete_tail_node method deletes items from the end of the list and preserves the order
    def test_delete_tail_method_on_two_player_list(self):
        def test_two_items_list_delete_tail(self):
            # Insert two nodes into the list.
            self.test_list.insert_tail_node(self.player1)
            self.test_list.insert_tail_node(self.player2)
            # Delete the tail node and store the deleted object.
            deleted_tail = self.test_list.delete_tail_node()
            # Confirm that the deleted node was player2 (the tail).
            self.assertIs(deleted_tail, self.player2)
            # Check that the tail is now player1.
            self.assertIs(self.test_list._tail.player, self.player1)
            # Check that the next node for player1 is None.
            self.assertIsNone(self.test_list._tail.next_player)

    def test_delete_item_by_key(self):
        # Insert players into the list
        self.test_list.insert_head_node(self.player1)
        self.test_list.insert_head_node(self.player2)
        self.test_list.insert_head_node(self.player3)
        # Delete player2 by its key/uid
        self.test_list.delete_player_node_by_key("10472204")
        # Check that the head is still player3
        self.assertIs(self.test_list._head.player, self.player3)
        # Check that the head's next node points to player1
        self.assertIs(self.test_list._head.next_player.player, self.player1)
        # Check that the tail is now player1
        self.assertIs(self.test_list._tail.player, self.player1)
        # Confirm that player1's previous node points to player3
        self.assertIs(self.test_list._tail.previous_player.player, self.player3)
        # Check that the player 3 doesn't have a previous player
        self.assertIsNone(self.test_list._head.previous_player)
        # Check that player 1 doesn't have a next player as it is the tail of this list
        self.assertIsNone(self.test_list._tail.next_player)
        # Check that the delete_player_node_by_key method fails when given a fake uid
        non_existent_player = self.test_list.delete_player_node_by_key("12345689")
        self.assertIsNone(non_existent_player)

