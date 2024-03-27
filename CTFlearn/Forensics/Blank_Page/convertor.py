file = open('TheMessage.txt', 'r')

string = file.read()


answer = string.replace(' ', '0').replace('\u200f', '1')

print(answer)

