#Commenting out so I can keep past record of what was changed.
#with open('sample.txt', 'r') as f:
#    for line in f:
#        print(line)

#there are line breaks in the code as the print() command adds a line break. Then there is a second one as 
#the file itself has line breaks,

#this removes the line breaks
#with open('sample.txt', 'r') as f:
#   for line in f:
#        print(line.strip())

#with open('output.txt', 'w') as f:
#    f.write("This is a new file. \n")
#    f.write("It has two lines. \n")

import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30"

print(re.findall(pattern, text))
    