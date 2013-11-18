import rg

from random import choice


class Robot:
    def act(self, game):
        locs = rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))
        return ['move', choice(locs)]
