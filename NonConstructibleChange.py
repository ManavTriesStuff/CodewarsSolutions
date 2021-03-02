def nonConstructibleChange(coins):
    coins.sort()
	change = 0
	
	for coin in coins:
		if coin > change + 1:
			return change + 1
		else:
			change += coin
	return change + 1
	