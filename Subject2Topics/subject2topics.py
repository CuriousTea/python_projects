## PROGRAM: The aim of this program is to turn topic level concepts of a given subject into their own markdown file for further conceptual differentiation. 

## WHY IMPORTANT: KEY terms UNLOCK a subjects knowledge, you could say. This filters them out from the 
## noise and endless deluge of words to a list you can focus on. Follow curiosity, satiate curiosity. Do your 
## own research. 


## Essentially, you are collecting the main chapter headings of a subject in list format on a subject.md file e.g;
## Python Strings
## Python Functions
## Python Classes

## Then we want to turn each line into it's own .md file automatically, giving us the ability to zoom in on a
## topic and topic related concepts. E.g program turns Python Classes into Python Classes.md which we can then further collect key terms as such:

## FILE: Python Classes.md
#  Class Definition
#  Class Objects
#  Instance Objects
#  Method Objects 
#  etc
#  etc 

## Place this script in in a folder structure like below:
## Folder structure: 
## Key-Terms
##   <script>
##   subjects
##   topics
## Explore error handling (maybe set up retrys for input) 
import os

# Get Subject File
nwd = os.chdir('subjects')
x = input('Enter Subject file name: ' )
for file in os.listdir():
    if file == x:
        subject = file

# Load file into memory
read = open(subject, "r")

# Create a subject folder in topics directory
os.chdir('../topics')
os.mkdir(f'{subject}', 755)

# Create individual markdown files for each topic
os.chdir(f'{subject}')
for line in read:
    y = line.strip()
    name = f"_{y}.md" 
    f = open(name, "a")


