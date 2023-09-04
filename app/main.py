from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode



def print_hi():
    p1 = Player("20069321", "Daniel")  # This creates an instance of the player object
    print(f"{p1}")  # This line prints that object to ensure the __str__ method is working correctly


def test_uid():
    player = Player("20069321", "Daniel")
    node = PlayerNode(player)
    uid = node.key
    print(uid)
    PlayerList.display(node)


def test_string_method():
    # create a PlayerList object
    player_list = PlayerList()

    # insert some players
    player_list.insert_head_node(Player("20069321", "Daniel"))
    player_list.insert_head_node(Player("10472204", "John"))
    player_list.insert_head_node(Player("29543305", "Brayden"))

    # call the display method to print the players in the list
    player_list.display(forward=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    test_string_method()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

