def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse = True)
	blueShirtHeights.sort(reverse = True)
	
	colorInFront = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
	
	for idx in range(len(blueShirtHeights)):
		redShirts = redShirtHeights[idx]
		blueShirts = blueShirtHeights[idx]
		
		if colorInFront == 'RED':
			if redShirts >= blueShirts:
				return False
		else:
			if blueShirts >= redShirts:
				return False
	
    return True