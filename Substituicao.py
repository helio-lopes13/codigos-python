def substituicao(A, A1, A2):
	if A == A1:
		return A2
	else:
		if len(A) == 1:
			return A
		if A[0] == '¬':
			return ('¬', substituicao(A[1], A1, A2))
		if type(A[1]) == str:
			return (substituicao(A[0], A1, A2), A[1], substituicao(A[2], A1, A2))

formula = (('¬', ('p', '>', 'q')), 'v', 'r')
form = ('p', '>', 'q')
subs = ('s', 'v', 't')

print('Formula original: ', formula, '\nFormula atualizada: ', substituicao(formula, form, subs))