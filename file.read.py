# with open ("theven.txt") as f
#by above syntax there will be no need for clasing the open leder
f = open("theven.txt")
content = f.read()
print(content)
# f.seek(7) #it will just reach that place and there will be at least one argument
# print(f.tell())
# print(f.readline())
#Code as discussed in the video
#   f = open("theven.txt", "rt")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = t.read(34455)
# print("2", content)
f.close()
