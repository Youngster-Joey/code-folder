import itertools

numbers = [7, 10, 6, 6, 13, 13]

operations = []

x = ["+", "-", "*", "/"]

for num in itertools.permutations(numbers):
	for ops in itertools.product(x, repeat = 5):
		expression = str(num[0]) + ops[0] + str(num[1]) + ops[1] + str(num[2]) + ops[2] + str(num[3]) + ops[3] + str(num[4]) + ops[4] + str(num[5])
		ans = num[0]
		for i in range(5):
			ans = eval(str(ans) + ops[i] + str(num[i + 1]))
		if ans == 163:
			print(expression)