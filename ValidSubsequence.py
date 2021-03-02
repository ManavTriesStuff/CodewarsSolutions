def isValidSubsequence(array, sequence):
    seqId = 0
	arrId = 0
	
	while arrId < len(array) and seqId < len(sequence):
		if array[arrId] == sequence[seqId]:
			seqId += 1
		arrId += 1
	return seqId == len(sequence)