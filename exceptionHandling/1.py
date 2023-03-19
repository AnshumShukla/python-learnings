try:
    fh = open("testfile.txt", "w")
    fh.write("This is my test file for exception handling!!")
    # try try but dont cry
except:
    print("Error: can't find file or read data")
    # exception raised
else:
    print("Written content in the file successfully")
    fh.close()
    # when no exception raised
finally:
    # runs everytime
    print("Here it goes")
  