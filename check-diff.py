import sys
from difflib import Differ 
  
with open(sys.argv[1]) as file_1, open(sys.argv[2]) as file_2: 
    differ = Differ() 
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()): 
        print(line)