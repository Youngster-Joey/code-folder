import itertools

numbers = [3, 3, 7, 7]

operations = []

x = ["+", "-", "*", "/"]

for num in itertools.permutations(numbers):
	for ops in itertools.product(x, repeat = 3):
		expression = str(num[0]) + ops[0] + str(num[1]) + ops[1] + str(num[2]) + ops[2] + str(num[3])
		ans = num[0]
		for i in range(3):
			ans = eval(str(ans) + ops[i] + str(num[i + 1]))
		if ans == 24:
			print(expression)