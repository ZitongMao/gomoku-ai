

def alpha_beta_prune(ai, alpha=-10000000, beta=10000000):
	if ai.__depth <= 0:
		return -ai.evaluate()
	for nextPlay, i, j in ai.generate():
		temp_score = -alpha_beta_prune(nextPlay, -beta, -alpha)
		if temp_score > beta:
			return beta
		if temp_score > alpha:
			alpha = temp_score
			ai.__currentI, ai.__currentJ = i, j
	return alpha
