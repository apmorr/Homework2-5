from hw5 import solveable, valid_moves
import unittest


class TestChessboard(unittest.TestCase):

    def test_valid_moves(self):
        self.assertCountEqual(valid_moves((0, 0)), {(1, 2), (2, 1)})
        self.assertCountEqual(valid_moves((2, 2)), {(0, 1), (0, 3), (1, 0), (1, 4), (3, 0), (3, 4), (4, 1), (4, 3)})
        self.assertCountEqual(valid_moves((7, 7)), {(5, 6), (6, 5)})

    def test_solveable(self):
        self.assertTrue(solveable({(1, 5), (2, 1), (2, 5), (4, 2), (5, 5), (6, 3)}, (3, 3)))
        self.assertFalse(solveable({(1, 3), (2, 1), (2, 5), (4, 2), (5, 5)}, (3, 3)))
        self.assertFalse(solveable({(1, 3), (2, 1), (2, 5), (4, 2), (5, 5), (6, 3)}, (0, 0)))
        self.assertTrue(solveable(set(), (3, 3)))

    unittest.main()
