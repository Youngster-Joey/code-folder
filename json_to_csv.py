import json

# Converts a Json from a particular e-commerce API to a CSV file
# THIS IS NOT AN ALL PURPOSE JSON TO CSV TOOL
# File locations are hardcoded, json keys such as 'value' are hardcoded, does not handle nested lists (although idk if csv supports that anyways)

file_location = ""

with open(file_location) as f:
	j = json.load(f)

with open('p21.csv', 'w') as f:
	for key in j['value'][0].keys():
		f.write(key + ', ')
	f.write('\n')

	for i in range(5): 
	# for i in range(len(j['value'])):
		for key in j['value'][i].keys():
			# wanted to overwrite item_desc for testing privacy purposes
			if key == 'item_desc':
				f.write("lorem ipsum, ")
			else: 
				f.write(str(j['value'][i][key]) + ', ')
		f.write('\n')