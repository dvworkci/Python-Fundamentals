# Reading files in python

# File modes : -
# open("movies.txt","r")      # r => read mode
# open("movies.txt","w")      # w => write mode
# open("movies.txt","a")      # a => append info at the eof
# open("movies.txt","r+")      # r+ => read and write

movies_file = open("movies.txt","r")
if(movies_file.readable()):
    # print(movies_file.read())
    # print(movies_file.readline()) # read by line
    # print(movies_file.readlines()) # makes an array of all lines

    # looping through each line inside the file
    for movie in movies_file.readlines():
        print(movie)
else:
    print("File is not readable")
movies_file.close()