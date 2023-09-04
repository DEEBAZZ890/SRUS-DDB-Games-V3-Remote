import unittest
from app.player import Player


class TestPlayerClassPasswordMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player("20069321", "Daniel")
        self.player.add_password("password")

    # Checks that the hashed password is generated and stored in the hashed password private variable
    def test_hashed_password_is_stored_after_add_password(self):
        self.assertIsNotNone(self.player._hashed_password)

    # Tests the functionality of the verify function
    def test_verify_password_returns_true_for_correct_password(self):
        self.assertTrue(self.player.verify_password("password"))

    def test_verify_password_returns_false_for_incorrect_password(self):
        self.assertFalse(self.player.verify_password("wrong_password"))

    # Check that the add_password method rejects an empty string and returns the validation message
    def test_add_password_fails_for_empty_string(self):
        # Pass the add_password an empty string and store the return message
        result = self.player.add_password("")
        # Check that the add_password method failed as expected and returned the validation message
        self.assertEqual(result, "No password entered. The player requires a password that is not empty")

    # Check to see that false is returned if an empty string is given to the verify_password method
    def test_verify_password_returns_false_for_empty_string(self):
        # Check that passing an empty string will trigger the false condition inside the verify_password method
        self.assertFalse(self.player.verify_password(""))

