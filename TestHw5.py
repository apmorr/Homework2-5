from hw5 import solveable, valid_moves
import unittest


class TestValidMoves(unittest.TestCase):

    def testValidMoves(self):
        self.assertEqual(valid_moves((0, 0)), {(1, 2), (2, 1)})
        self.assertEqual(valid_moves((2, 2)), {(0, 1), (0, 3), (1, 0), (1, 4), (3, 0), (3, 4), (4, 1), (4, 3)})
        self.assertEqual(valid_moves((7, 7)), {(5, 6), (6, 5)})


class TestSolveable(unittest.TestCase):

    def testUnsolveable(self):
        """Test a few unsolveable puzzles"""
        self.assertFalse(solveable({(1, 3), (2, 1), (2, 5), (4, 2), (5, 5)}, (3, 3)))
        self.assertFalse(solveable({(1, 3), (2, 1), (2, 5), (4, 2), (5, 5), (6, 3)}, (0, 0)))

    def testSolveableSimple(self):
        """Test a simple solveable puzzle"""
        self.assertTrue(solveable({(1, 3), (2, 1), (4, 2)}, (2, 3)))
        self.assertTrue(solveable({(1, 4), (2, 2), (3, 5), (4, 1), (6, 2)}, (5, 4)))

    def testSolveableHard(self):
        """Test a few more complex solveable puzzles - try to break your recursive algorithm to help you catch any
        mistakes"""
        self.assertTrue(solveable(
            {(0, 6), (1, 3), (2, 0), (2, 1), (2, 5), (2, 7), (3, 5), (4, 1), (4, 2), (5, 4), (6, 2), (6, 6), (7, 4)},
            (2, 3)))


if __name__ == '__main__':
    unittest.main()
