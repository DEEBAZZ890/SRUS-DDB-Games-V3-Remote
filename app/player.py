from argon2 import PasswordHasher, exceptions


class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid  # A unique id for the player
        self._name = name  # The name of the player
        self._hashed_password = None  # stores the hashed version of the players password

    def add_password(self, password):  # Takes the plaintext password as a parameter and hashes it using Argon2
        if not password:  # checks if the parameter given is None or an empty string
            return "No password entered. The player requires a password that is not empty"
        else:
            ph = PasswordHasher()
            hash_value = ph.hash(password)
            self._hashed_password = hash_value

    def verify_password(self, password):
        ph = PasswordHasher()
        try:
            ph.verify(self._hashed_password, password)
            return True
        except exceptions.VerifyMismatchError:
            return False

    @property  # getter for uid
    def uid(self):
        return self._uid

    @property  # getter for name
    def name(self):
        return self._name


def __str__(self):  # used to print readable string of the player object
    return f"{self._uid} - {self._name}"


def __repr__(self):
    class_name = self.__class__.__name__
    return f'{class_name}(uid={self.uid!r}, name={self.name!r})'
