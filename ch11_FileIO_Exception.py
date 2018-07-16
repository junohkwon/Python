# # write file
# myfile = open('C:\\Users\\DS부문 머신러닝 아카데미\\Desktop\\foo.txt','w+')
#
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n"%i
#     myfile.write(data)
#
# myfile.close()

# # append line
# myfile = open('C:\\Users\\DS부문 머신러닝 아카데미\\Desktop\\foo.txt','a')
#
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n"%i
#     myfile.write(data)
#
# myfile.close()

# # read
# myfile = open('C:\\Users\\DS부문 머신러닝 아카데미\\Desktop\\foo.txt','r')
#
# lines = myfile.read()
# print(lines)
#
# myfile.close()

# # read line
# myfile = open('C:\\Users\\DS부문 머신러닝 아카데미\\Desktop\\foo.txt','r')
#
# line = myfile.readline()
# print(line)
#
# myfile.close()

# # read line (while)
# myfile = open('C:\\Users\\DS부문 머신러닝 아카데미\\Desktop\\foo.txt','r')
#
# while True:
#     line = myfile.readline()
#     if not line: break
#     print(line)
#
# myfile.close()

# # read lines
# myfile = open('C:\\Users\\DS부문 머신러닝 아카데미\\Desktop\\foo.txt','r')
#
# lines = myfile.readlines()
#
# for l in lines:
#     print(l)
#
# myfile.close()

# with open('foo.txt','w') as f:
#     f.write("life is too short, you need python")

# with open('pi_digit.txt','r') as f:
#     contents = f.read()
#     print(contents)

# with open('pi_digit.txt','r') as f:
#     for line in f:
#         print(line)

# with open('pi_digit.txt','r') as f:
#     for line in f:
#         print(line.rstrip())  ## rstrip()이 \n 마크도 없애버림

# with open('pi_digit.txt','r') as f:
#     lines = f.readlines()
#     str=''
#     for l in lines:
#         str += l.rstrip()
#     print(str)
#     print(len(str))


try:
    x=5+'ham'
except TypeError:
    print('darn it')
finally:
    print('lets go further')