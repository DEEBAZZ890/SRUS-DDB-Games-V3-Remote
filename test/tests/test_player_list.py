import unittest
from app.player_list import PlayerList
from app.player import Player


class TestPlayerListClass(unittest.TestCase):

    def setUp(self) -> None:
        self.test_list = PlayerList()
        self.player1 = Player("20069321", "Daniel")
        self.player2 = Player("10472204", "John")
        self.player3 = Player("29543305", "Brayden")

    def test_insert_head_into_empty_list(self):
        """Confirm single insert is elected as head node when function is called"""
        self.assertIsNone(self.test_list._head)
        self.test_list.insert_head_node(self.player1)
        self.assertIs(self.test_list._head.player, self.player1)
        self.assertIsNone(self.test_list._head.next_player)
        self.assertIsNone(self.test_list._head.previous_player)

    def test_insert_head_on_list_with_contents(self):
        """Test that the second player is made to be the head"""
        self.test_list.insert_head_node(self.player1)
        self.test_list.insert_head_node(self.player2)
        self.assertEqual(self.test_list._head.player, self.player2)
        self.assertEqual(self.test_list._head.next_player.player, self.player1)
        self.assertIsNone(self.test_list._head.previous_player)
        self.assertEqual(self.test_list._head.next_player.previous_player.player, self.player2)

    def test_tail_insert_on_list(self):
        """Test multiple tail insert and ensure the tail is updated appropriately"""
        self.test_list.insert_tail_node(self.player1)
        self.assertIs(self.test_list._head.player, self.player1)
        self.assertIs(self.test_list._tail.player, self.player1)

        self.test_list.insert_tail_node(self.player2)
        self.assertIs(self.test_list._head.player, self.player1)
        self.assertIs(self.test_list._tail.player, self.player2)
        self.assertIs(self.test_list._head.next_player.player, self.player2)

        self.test_list.insert_tail_node(self.player3)
        self.assertIs(self.test_list._head.player, self.player1)
        self.assertIs(self.test_list._tail.player, self.player3)
        self.assertIs(self.test_list._head.next_player.player, self.player2)
        self.assertIs(self.test_list._head.next_player.next_player.player, self.player3)

    def test_delete_head_on_empty_list(self):
        self.assertRaises(ValueError, self.test_list.delete_head_node)
        self.assertIsNone(self.test_list._head)
        self.assertIsNone(self.test_list._tail)

    def test_delete_head_item_from_list(self):
        self.test_list.insert_head_node(self.player1)
        self.test_list.delete_head_node()
        self.assertIsNone(self.test_list._head)
        self.assertIsNone(self.test_list._tail)

    def test_delete_head_method_on_three_player_list(self):
        self.test_list.insert_head_node(self.player3)
        self.test_list.insert_head_node(self.player2)
        self.test_list.insert_head_node(self.player1)

        self.assertIs(self.test_list._head.player, self.player1)
        self.test_list.delete_head_node()

        self.assertIs(self.test_list._head.player, self.player2)
        self.test_list.delete_head_node()

        self.assertIs(self.test_list._head.player, self.player3)
        self.test_list.delete_head_node()

        self.assertIsNone(self.test_list._head)
        self.assertIsNone(self.test_list._tail)

    def test_delete_tail_method_on_two_player_list(self):
        self.test_list.insert_tail_node(self.player1)
        self.test_list.insert_tail_node(self.player2)
        self.test_list.delete_tail_node()
        self.assertIs(self.test_list._tail.player, self.player1)
        self.assertIsNone(self.test_list._tail.next_player)

    def test_delete_item_by_key(self):
        self.test_list.insert_head_node(self.player1)
        self.test_list.insert_head_node(self.player2)
        self.test_list.insert_head_node(self.player3)

        self.test_list.delete_player_node_by_key("10472204")

        self.assertIs(self.test_list._head.player, self.player3)
        self.assertIs(self.test_list._tail.player, self.player1)

        self.assertRaises(ValueError, self.test_list.delete_player_node_by_key, "12345689")
