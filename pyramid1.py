from termcolor import colored;
from colorama import init;

init();

'''
LIST COMPREHENSION COMBINED WITH .join().
'''
ListComprehensionPyramidBuilder = lambda character, rows: "\n".join([character*(i+1) for i in range(rows)]); #list comprehension.
print(ListComprehensionPyramidBuilder("X", 5))

print("\n")

'''
RECURSION.
'''
def RecursionPyramidBuilder(character, rows):
   color = "red" if (rows%2==1) else "light_green";
   """
   Builds a pyramid using RECURSION.
   """
   if rows<2:
      return colored(character, color, attrs=['bold']) + "\n";
   #The base PyramidBuilder(character, rows-1) will ALWAYS end with a new line. Then, below that, we have {character * rows remaining} that signifies the end of that iteration.
   return colored(f"{RecursionPyramidBuilder(character, rows-1)}", color, attrs=['bold']) + colored(character*rows, color, attrs=['bold']) + "\n";
print(RecursionPyramidBuilder("*", 5))

print("\n")

'''
REGULAR LOOPS.
'''
def LoopPyramidBuilder(character, rows):
   pyramid = "";
   for i in range(rows):
      pyramid = pyramid + (character*i) + "\n"
   return pyramid;

print(LoopPyramidBuilder("O", 5))



