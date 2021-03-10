def getNthFib(n):
    lastTwo = [0,1]
	counter = 3
	while counter <=n:
		nextNum = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextNum
		counter += 1
	return lastTwo[1] if n>1 else lastTwo[0]