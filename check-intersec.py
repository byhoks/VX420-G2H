import sys
from difflib import Differ 
  
with open(sys.argv[1]) as file_1, open(sys.argv[2]) as file_2: 
    differ = Differ() 
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()): 
        print(line)
[bobby.hoksono@jumpbox tp-link]$ cat check-intersec.py 
from __future__ import print_function
import sys
# Open File in Read Mode 
file_1 = open(sys.argv[1], 'r') 
file_2 = open(sys.argv[2], 'r') 

print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n') 

file_1_line = file_1.readline() 
file_2_line = file_2.readline() 

# Use as a Counter 

line_no = 1

print() 

with open(sys.argv[1]) as file1: 
        with open(sys.argv[2]) as file2: 
                same = set(file1).intersection(file2) 

print("Common Lines in Both Files") 

for line in same: 
        print(line, end='') 

print('\n') 
print("Difference Lines in Both Files") 
while file_1_line != '' or file_2_line != '': 

        # Removing whitespaces 
        file_1_line = file_1_line.rstrip() 
        file_2_line = file_2_line.rstrip() 

        # Compare the lines from both file 
        if file_1_line != file_2_line: 

                # otherwise output the line on file1 and use @ sign 
                if file_1_line == '': 
                        print("@", "Line-%d" % line_no, file_1_line) 
                else: 
                        print("@-", "Line-%d" % line_no, file_1_line) 

                # otherwise output the line on file2 and use # sign 
                if file_2_line == '': 
                        print("#", "Line-%d" % line_no, file_2_line) 
                else: 
                        print("#+", "Line-%d" % line_no, file_2_line) 

                # Print a empty line 
                print() 

        # Read the next line from the file 
        file_1_line = file_1.readline() 
        file_2_line = file_2.readline() 

        line_no += 1

file_1.close() 
file_2.close()