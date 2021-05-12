from solverFuncs import *

def main():
   row = 0
   col = 0 
   cages = get_cages()
   puzzle = []
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   puzzle.append([0, 0, 0, 0, 0])
   checks = 0
   backtracks = 0
   while row < 5:      
      puzzle[row][col] += 1 
      checks += 1 
      if check_valid(puzzle, cages): 
         if col < 4: 
            col += 1
         else:
            row += 1
            col = 0
      else: 
         while puzzle[row][col] >= 5:
            puzzle[row][col] = 0
            if col == 0: 
               row -= 1
               col = 4
               backtracks += 1
            else:
               col -= 1
               backtracks += 1

   print('\n--Solution--\n')

   for i in range(len(puzzle)): 
      for j in range(5):
         puzzle[i][j] = str(puzzle[i][j])
      print(' '.join(puzzle[i]))
   print('\nchecks:', checks, 'backtracks:', backtracks)
 
if __name__ == '__main__':
   main()