# A. S. M. Ahsan-Ul-Haque
# ahsanhaquetarique@gmail.com

# use python 3 to run this script
# this script shows a list of 15 unique video songs (if found) 
# that can make a user cry
# both in the console and saves the same in a file named youtubeLinks.txt
# in the same directory as the script 



# check for correct python version 
import sys
if sys.version_info < (3,):
  try:
    raise Exception("Must use python 3.x!")
  except Exception as e:
    print("You must use python 3.x to run this script!")
    sys.exit()



#python 3 code
from urllib import request
from urllib import parse
from re import *

def search():
  try:
    searchString = parse.urlencode({"search_query" : "sad english songs"})
    allContents = request.urlopen("http://www.youtube.com/results?" + searchString)
    results = findall(r'href=\"\/watch\?v=(.{11})', allContents.read().decode())
  except Exception as e:
    print("Network exception occured. Make sure you are connected to the internet!")
    sys.exit()
  print(len(results))
  showInConsole(results)
  writeFile(results)
  return

################
def showInConsole(results):
  dictionary = {}
  count = 0
  for vid in results:
    if(vid in dictionary):
      continue
    else:
      count = count + 1
      dictionary[vid] = count
      print("http://www.youtube.com/watch?v=" + vid)
      #if(count==15):
      #  break
  
  if(count < 15):
    print("15 unique videos not found!")

  return

################
def writeFile(results):
  dictionary = {}
  count = 0
  try:
    with open('youtubeLinks.txt', 'w') as f:
      for vid in results:
        if(vid in dictionary):
          continue
        else:
          count = count + 1
          dictionary[vid] = count
          f.write("http://www.youtube.com/watch?v=" + vid + "\n")
          #if(count==15):
          #  break
  except Exception as e:
    print("Error while writing to file youtubeLinks.txt, make sure you have the write permission in current directory!")
    return
  
  if(count < 15):
    print("15 unique videos not found!")

  print("\nLinks have been successfully written to youtubeLinks.txt, check for the file in current directory!")
  return

################  
def main():
    search()
    return


if __name__ == "__main__":
  main()

  
    
