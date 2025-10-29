#ProcessData.py
#Name: Michelle Diaz
#Date: 10/29/2025
#Assignment: Process Data

def makeID(first_name, last_name, student_id):
  user_id = first_name[0]  # first initial

  user_id += last_name

  # if last name less than 5 characters long, fill with 'X' until it's 5 characters long
  if len(last_name) < 5:
    user_id += 'X' * (5 - len(last_name))

  user_id += student_id[-3:]  # add last 3 characters from student id #

  return user_id

def main():

  abbreviateYear = {"Freshman": "FR", "Sophomore": "SO", "Junior": "JR", "Senior": "SR"}

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    # First name	Last Name	E-Mail	Student ID	Date of Birth	Year	Major

    info = line.split()
    first_name = info[0]
    last_name = info[1]
    student_id = info[3]
    year = info[5]
    major = info[6]

    user_id = makeID(first_name, last_name, student_id)
    major_year = major[:3] + '-' + abbreviateYear[year]

    outFile.write(first_name + ',' + last_name + ',' + user_id + ',' + major_year + '\n')

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()


if __name__ == '__main__':
  main()
