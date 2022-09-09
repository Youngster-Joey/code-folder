def greedy_seach(n, m):
	box_count = 0
	while len(n) > 0:
		this_box_capacity = 0
		flag = True
		while flag:
			largest = 0
			for item in n:
				if item <= m - this_box_capacity and item > largest:
					largest = item
			if largest == 0:
				flag = False
			else:
				n.remove(largest)
				this_box_capacity += largest
		box_count += 1
	return box_count

items = [15, 10, 5, 7, 6, 2, 6, 6, 2, 1, 5, 11, 4, 6, 6]
print(greedy_seach(items, 15))
