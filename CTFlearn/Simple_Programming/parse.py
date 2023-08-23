file = open("data.dat", "r")

string = file.read()

string = string.split()

cnt = []
for i in string:
    if i.count('0') % 3 == 0 or i.count('1') % 2 == 0:
        cnt.append(string.index(i))

print(len(cnt))


