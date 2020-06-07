def conectivos(A, atomicas):
	if len(A) == 1:
		return 0
	if A[0] == '¬':
		return conectivos(A[1], atomicas) + 1
	if type(A[1]) == str:
		return conectivos(A[0], atomicas) + 1 + conectivos(A[2], atomicas)


A = ['¬', ['p', 'v', 'q']]
atomicas = ['p', 'q']
print('Número de conectivos na fórmula: ', conectivos(A, atomicas))
