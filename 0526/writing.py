"""
# file writing 

file = open("file.txt", "w")

for i in range(1, 6):
    data = "HIIIII \n"
    file.write(data)

print("writed")
print(file.name)
file.close() # file 종료

file2 = open("file.txt","r")
msg = file2.readline() #라인한줄

while True :
    msg2 = file2.readline()
    if not msg2 : break # false ('')이어서 while종료
    print(msg2)
file2.close()

print(msg)

file3 = open("file.txt","r")
lines = file3.readlines() #list반환
print(lines)
for line in lines:
    print(line)

file3.close()

file4 = open("file.txt","r")
lines = file4.read()
print(lines)
file4.close()

file5 = open("file.txt",'a')
for i in range(3):
    i = "Heeeeello \n"
    file5.write(i)
file5.close()
"""
with open("foo.txt",'w') as f:
    f.write("Life is too short, you need python")
# 자동 생성 & 클로징
