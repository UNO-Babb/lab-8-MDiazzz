#ProcessData.py
#Name: Michelle Diaz
#Date: 10/28/2025
#Assignment: Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
   

   for line in inFileFile:
    info = line.split(",")
    first_name = info [0]
    last_name = info [1]
    user_ID = info [] 
    major_year = info []
    
  OutFile = open("names.dat",'w')

    for line in team_data:
    output = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," +line[5] + "," + "\n"
    OutFile.write(str(line))

OutFile.close() 

 myFile.close()

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()


if __name__ == '__main__':
  main()
if __name__ == '__main__':
  main()
