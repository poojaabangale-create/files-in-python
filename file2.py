file=open("condingal.txt","r")
#print(file.read())
file.close()




file_write=open('condingal.txt','w')

file_write.write("file in write mode ....")
file_write.write("im cube solving champain")
file_write.close()


file_append=open('condingal.txt','a')

file_append.write("\n file in append mode ....")
file_append.write("my cube collection is good")
file_append.close()
