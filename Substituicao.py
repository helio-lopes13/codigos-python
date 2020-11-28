def substituicao(A, B, C):
	if A == B:
		return C
	else:
		if len(A) == 1:
			return A
		if A[0] == '¬':
			return ('¬', substituicao(A[1], B, C))
		if type(A[1]) == str:
			return (substituicao(A[0], B, C), A[1], substituicao(A[2], B, C))

formula = (('¬', ('p', '>', 'q')), 'v', 'r')
form = ('p', '>', 'q')
subs = ('s', 'v', 't')

print('Formula original: ', formula, '\nFormula atualizada: ', substituicao(formula, form, subs))
