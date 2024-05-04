# # Reading Text Files

# with open('./test.txt', 'r') as file:
#     text = file.read()
#     print(text)

# # Writing to the saved file

# with open('./test.txt', 'w') as file:
#     file.write("This is a newly added line3")

# # Append to existing file

# with open('./test.txt', 'a') as file:
#     file.write('\nThis is a new line added using append method')
#     file.write('\nThis is a new line2 added using append method')

# #Manually inserting into a binary file
# with open ('./test.bin', 'wb') as file:
#     var = bytes([0x48, 0x65, 0x6C,0x6C, 0x6F])
#     file.write(var)

# #installing python packages


# import pickle

# data = "Hello"

# with open('./test.pickle', 'wb') as file:
#     pickle.dump(data, file)

with open('./test.pickle', 'rb') as file:
    bianry = file.read()
    print(bianry)




    


