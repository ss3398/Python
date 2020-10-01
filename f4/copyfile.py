srcfile = input("Enter source file name : ")
targetfile = input("Enter target file name : ")
srcfo = open(srcfile, "r")
targetfo = open(targetfile, "w")
all_of_it = srcfo.read()
targetfo.write(all_of_it)
srcfo.close()
targetfo.close()

