import rg

from random import choice


class Robot:
    def act(self, game):
        locs = rg.locs_around(self.location, filter_out=('invalid', 'obstacle', 'spawn'))
        return ['move', choice(locs)]
