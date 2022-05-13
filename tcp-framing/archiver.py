import sys, os

#fd = os.open("test.txt", os.O_RDWR)
#code = os.read(fd, os.path.getsize(fd))
#print("Encoded file:\n", code)

def writeByteArray(fileName):
    files = fileName.split(' ')
    bArray = bytearray()
    for i in files:
        with open(i, "rb") as file: 
   # fd = os.open(fileName, os.O_RDWR) 
   # encoded = os.read(fd, os.path.getsize(fd)
            bArray += file.read() 
   # os.write(fd1, bArray)
   # print("Decoding file")
   # decode(fd, encoded)
            
    return bArray
    	
def readByteArray(fd, bArray):
    with open(fd, "wb") as file:
        print(file.write(bArray))
       
        

#fileN = input("Input File Name: ")
#files = fileN.split(' ')
#bArray = writeByteArray(files)
#print("Encoded Files: ", bArray)

#print("Decoding Files...")
#for i in files:
#    readByteArray(i, bArray)
#    with open(i , 'r') as file:
#        print(file.read())
#encode length of each file
#encode a file and write it to stdout
#decode a file
#multiple files (append to byte array, )
