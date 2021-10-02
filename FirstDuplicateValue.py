# O(n) time | O(n) space
def firstDuplicateValue(array):
    values = {}
	for num in array:
		if num not in values:
			values[num] = True
		else:
			return num		
    return -1
