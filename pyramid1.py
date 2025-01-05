from termcolor import colored;
from colorama import init;
from time import sleep;

init();

MakeColored = lambda string, color='red': colored(string, color, attrs=['bold']); #colors words.

'''
LIST COMPREHENSION COMBINED WITH .join().
'''
print(f"Pyramid Builder using {MakeColored('.join()', 'light_red')} AND {MakeColored('LIST COMPREHENSION!!!', 'light_red')}");
ListComprehensionPyramidBuilder = lambda character, rows: "\n".join([character*(i+1) for i in range(rows)]); #list comprehension.
print(ListComprehensionPyramidBuilder("X", 5))

print()
sleep(1.75);

'''
RECURSION.
'''
print(f"Python Pyramid Builder using the power of {MakeColored('RECURSION', 'light_yellow')}!!!")
def RecursionPyramidBuilder(character, rows):
   color = "red" if (rows%2==1) else "light_green";
   """
   Builds a pyramid using RECURSION.
   """
   if rows<2:
      return colored(character, color, attrs=['bold']) + "\n";
   #The base PyramidBuilder(character, rows-1) will ALWAYS end with a new line. Then, below that, we have {character * rows remaining} that signifies the end of that iteration.
   return MakeColored(f"{RecursionPyramidBuilder(character, rows-1)}", color) + MakeColored(character*rows, color) + "\n"
print(RecursionPyramidBuilder("x", 10))

print()
sleep(1.75);

'''
REGULAR LOOPS.
'''
print(f"Python Pyramid Builder using regular {MakeColored('FOR LOOP', 'light_green')} that actually returns something!!!")
def LoopPyramidBuilder(character, rows):
   pyramid = "";
   for i in range(rows):
      pyramid = pyramid + (character*i) + "\n" if i !=0 else pyramid + (character*i);
   return pyramid;
print(LoopPyramidBuilder("O", 5))

print()
sleep(1.75);

'''
Using Enums!!!
'''
print(f"'E'ntroding... The {colored('ENUMERATING PYRAMID', 'light_green', attrs=['bold'])}!!!")
def EnumeratingPyramid(character, rows):
   pyramid = list(enumerate([character for _ in range(rows)], 1));
   return "".join([f"{i[1]*i[0]}\n" for i in pyramid]);

print(EnumeratingPyramid("^", 9));



