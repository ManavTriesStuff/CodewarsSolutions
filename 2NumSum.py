# def twoNumberSum(array, targetSum):
# 	nums = {}
# 	for i in array:
# 		rem = targetSum - i
# 		if rem in nums:
# 			return [i,rem]
# 		else:
# 			nums[i] = True
# 	return []

	def twoNumberSum(array, targetSum):
    array.sort()
	left = 0
	right = len(array) - 1 
	
	while left < right:
		currSum = array[left] + array[right]

		if currSum == targetSum:
			return [array[left],array[right]]
		elif currSum < targetSum:
			left +=1
		elif currSum > targetSum:
			right -=1
	
	return []