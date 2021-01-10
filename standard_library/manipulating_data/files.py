# fp = open('testfile.txt', 'w')
# fp.write("This is some text")

# fp.close()


# with open ('testfile.txt', 'r') as fp:
#     data = fp.read()
#     print(data)

with  open('testfile.txt', 'a+') as fp:
    fp.write("New data added to the file\n")
    fp.seek(0)
    data = fp.read()
    print(data)