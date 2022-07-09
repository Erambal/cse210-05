import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.segment import Segment


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.
    """
    def __init__(self, start_x, start_y):

        super().__init__()
        self._segments = []
        self._prepare_body(start_x, start_y)

    def get_segments(self):
        return self._segments

    def set_is_dead(self):
        self._is_dead = True


    def get_color(self):
        if super()._is_dead:
            return constants.WHITE
        else:
            return super().get_color()

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        self.grow_tail(1)
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Segment(self)
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._is_dead:
                segment.set_color(constants.WHITE)
            else:
                segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, start_x = 0, start_y = 0):
        x = start_x   #int(constants.MAX_X / 2)
        y = start_y   #int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 1)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Segment(self)
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)