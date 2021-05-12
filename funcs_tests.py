import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
   def test_check_row(self):
      row = [1, 2, 3, 4, 5]
      self.assertTrue(check_row(row), True)
   def test_check_row1(self):
      row = [1, 2, 1, 4, 5]
      self.assertFalse(check_row(row), False)

   def test_check_row2(self):
      row = [1, 0, 0, 0, 0]
      self.assertTrue(check_row(row), True)

   def test_check_rows(self):
      puzzle = []
      puzzle.append([5, 1, 2, 5, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_rows_valid(puzzle), False)

   def test_check_rows1(self):
      puzzle = []
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle), True)

   def test_check_column(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_column(puzzle, 0), True)

   def test_check_column1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([1, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_column(puzzle, 0), False)

   def test_check_columns(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_columns_valid(puzzle), True)

   def test_check_columns1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([5, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_columns_valid(puzzle), False)

   def test_check_columns2(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 0])
      puzzle.append([3, 0, 0, 1, 0])
      puzzle.append([0, 0, 3, 0, 0])
      self.assertFalse(check_columns_valid(puzzle), False) 

   def test_check_columns3(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 6])
      self.assertFalse(check_columns_valid(puzzle), False)

   def test_square_to_row1(self):
      self.assertEqual(square_to_row(14), 2)
   def test_square_to_row2(self):
      self.assertEqual(square_to_row(0), 0)

   def test_square_to_col1(self):
      self.assertEqual(square_to_col(17, 3), 2)
   def test_square_to_col2(self):
      self.assertEqual(square_to_col(24, 4), 4)

   def test_check_cage1(self):
      cage = [8, 3, 0, 1, 2]
      puzzle = []
      puzzle.append([5, 3, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_cage(puzzle, cage), False)

   def test_check_cage2(self):
      cage = [8, 3, 0, 1, 2]
      puzzle = []
      puzzle.append([5, 0, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_cage(puzzle, cage), True)

   def test_check_cage3(self):
      cage = [8, 3, 4, 9, 14]
      puzzle = []
      puzzle.append([5, 3, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 4])
      puzzle.append([2, 3, 0, 5, 5])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_cage(puzzle, cage), False)

   def test_check_cages1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_cages_valid(puzzle, cages))

   def test_check_cages2(self): 
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([1, 4, 5, 2, 3])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      cages.append([15, 5, 20, 21, 22, 23, 24])
      self.assertTrue(check_cages_valid(puzzle, cages))

   def test_check_cages4(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([3, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      cages.append([5, 2, 20, 21])
      self.assertTrue(check_cages_valid(puzzle, cages))

   def test_check_valid0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertTrue(check_valid(puzzle, cages))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()