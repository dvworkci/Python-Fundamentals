# Writing to file in python
# movies_file = open("movies.txt","w")    # This mode will overwrite all pre-existing info
movies_file = open("movies.txt","a")    # This mode will overwrite all pre-existing info
if(movies_file.writable()):
    movies_file.write("\nTitanic => James Cameron")
    print("Write successful")
else:
    print("File is not readable")
movies_file.close()