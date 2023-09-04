import unittest
from app.player import Player


class TestPlayerPrivateInstanceVariables(unittest.TestCase):
    def setUp(self) -> None:
        # Set the properties for the player here just for maintainability purposes
        self.test_uid = "20069321"
        self.test_name = "Daniel"
        self.player = Player(self.test_uid, self.test_name)  # Create a test player that contains a name and uid

    # Checks that player id is added successfully
    def test_uid_is_created(self):
        # Uses the getter for uid and checks if the UID matches the UID for the player
        self.assertEqual(self.player.uid, self.test_uid)

    # Checks that player name is added successfully
    def test_name_is_created(self):
        # Using the getter property, checks that the name was assigned correctly for the player
        self.assertEqual(self.player.name, self.test_name)

