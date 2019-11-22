expected_value = []
value = 0
while len(expected_value) < 10:
	print (expected_value)
	value = value + 1
	expected_value.append(value)
	

if len(expected_value) == 0:
	print ('wrong')
