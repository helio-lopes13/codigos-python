def atomicas(A):
	if len(A) == 1:
		return set(A)
	if A[0] == '¬':
		return atomicas(A[1])
	if type(A[1]) == str:
		return atomicas(A[0]).union(atomicas(A[2]))

def qtdAtomicas(A):
	if len(A) == 1:
		return 1
	if A[0] == '¬':
		return qtdAtomicas(A[1])
	if type(A[1]) == str:
		return qtdAtomicas(A[0]) + qtdAtomicas(A[2])

formula = (('p', '^', ('¬', ('p', '>', ('¬', 'q')))), 'v', ('¬', 'q'))
print('Conjunto de atomicas na fórmula', formula, ':', atomicas(formula), '\nNúmero de atomicas na fórmula: ', qtdAtomicas(formula))