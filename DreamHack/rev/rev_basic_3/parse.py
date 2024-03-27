num = ['49','60','67','74','63','67','42','66','80','78','69','69','7B','99','6D','88','68','94','9F','8D','4D','A5','9D','45']
ans = ""

for i in range(24):
	temp = (int(num[i], 16) - (2 * i)) ^ i
	ans += chr(temp)


#for i in ans:
#    print(chr(i), end=" ")
print(ans)

