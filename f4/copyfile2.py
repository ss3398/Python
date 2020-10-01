srcfile = input("Enter source file name : ")
targetfile = input("Enter target file name : ")
srcfo = open(srcfile, "rb")
targetfo = open(targetfile, "wb")
all_of_it = srcfo.read()
targetfo.write(all_of_it)
srcfo.close()
targetfo.close()

