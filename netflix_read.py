#Modules
import os
import csv

video = input("What show or movie are you looking for? ")


# Set path for file
file_path =os.path.join("Class_work_02_09_python\\Resources","netflix_ratings.csv")

print(file_path)
#file_path

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    x=0
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])
            x=x+1
            break
    if x==0:
        print("Sorry about this, we don't seem to have what you are looking for!")

      

