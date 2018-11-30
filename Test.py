import unittest

import LCD


class Test(unittest.TestCase):

    def test_zero_gives_zero(self):
        self.assertEqual("._.\n|.|\n|_|", LCD.drawer(0))

    def test_ten_gives_ten(self):
        self.assertEqual("... ._.\n..| |.|\n..| |_|", LCD.drawer(10))
