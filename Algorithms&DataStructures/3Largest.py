def findThreeLargestNumbers(array):
    out = [None,None,None]
	for num in array:
		updateLargest(out,num)
	return out

def updateLargest(out,num):
	if out[2] == None or num>out[2]:
			shift(out,num,2)
	elif out[1] == None or num>out[1]:
			shift(out,num,1)
	elif out[0] == None or num>out[0]:
			shift(out,num,0)
			
			
def shift(array,num,idx):
	for i in range(idx+1):
		if i ==idx:
			array[i] = num
		else:
			array[i] = array[i+1]