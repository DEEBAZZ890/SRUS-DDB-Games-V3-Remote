from typing import Optional
from argon2 import PasswordHasher, exceptions


class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid = uid  # A unique id for the player
        self._name = name  # The name of the player
        self._hashed_password: Optional[str] = None  # stores the hashed version of the players password

    @property  # getter for uid
    def uid(self) -> str:
        return self._uid

    @property  # getter for name
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:  # used to print readable string of the player object
        return f"UID:{self._uid} NAME: {self._name}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(uid={self.uid!r}, name={self.name!r})'

    def add_password(self, password: str) -> None:
        if not password.strip():
            raise ValueError("No password entered. The player must have a password")
        else:
            ph = PasswordHasher()
            hash_value = ph.hash(password)
            self._hashed_password = hash_value

    def verify_password(self, password: str) -> bool:
        ph = PasswordHasher()
        try:
            ph.verify(self._hashed_password, password)
            return True
        except exceptions.VerifyMismatchError:
            return False