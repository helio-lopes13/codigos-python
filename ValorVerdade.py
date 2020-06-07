def valor_verdade(phi, verdade):
	if len(phi) == 1:
		return verdade[phi]
	if phi[0] == '¬':
		return not valor_verdade(phi[1], verdade)
	if type(phi[1]) == str:
		if phi[1] == '^':
			return valor_verdade(phi[0], verdade) and valor_verdade(phi[2], verdade)
		if phi[1] == 'v':
			return valor_verdade(phi[0], verdade) or valor_verdade(phi[2], verdade)
		if phi[1] == '>':
			if valor_verdade(phi[0], verdade) == True and valor_verdade(phi[2], verdade) == False:
				return False
			else:
				return True

formula = [['p', '^', 'q'], '>', ['s', 'v', 'r']]
truth = {'p': True, 'q': True, 'r': False, 's': True}
print('Valor verdade da expressão ', formula,': ', valor_verdade(formula, truth))