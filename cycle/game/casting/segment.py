import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Segment(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, head):

        super().__init__()
        self._head = head

    def get_color(self):
        if self._head.get_is_dead():
            return constants.WHITE
        else:
            return super().get_color()

    def get_head(self):
        return self._head

