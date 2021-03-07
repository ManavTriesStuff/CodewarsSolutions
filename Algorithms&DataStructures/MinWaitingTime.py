def minimumWaitingTime(queries):
    queries.sort()
	minTime = 0
	
	for idx, duration in enumerate(queries):
		queriesRemaining = len(queries) - (idx+1)
		minTime += queriesRemaining * duration 
	return minTime
