def updateScore(team,points,scores):
	if team not in scores:
		scores[team] = 0
	
	scores[team] += points

def tournamentWinner(competitions, results):
	bestTeam = ""
    scores = {bestTeam:0}
	
	for idx, competition in enumerate(competitions):
		res = results[idx] 
		homeTeam, awayTeam = competition
		
		winner = homeTeam if res == 1 else awayTeam
		
		updateScore(winner, 3, scores)
		
		if scores[winner] > scores[bestTeam]:
			bestTeam = winner
	
	return bestTeam


	