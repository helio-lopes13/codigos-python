def subformulas(phi, atomicas):
	if len(phi) == 1:
		return set(phi)
	if phi[0] == '¬':
		return {phi}.union(subformulas(phi[1], atomicas))
	if type(phi[1]) == str:
		return {phi}.union(subformulas(phi[0], atomicas)).union(subformulas(phi[2], atomicas))


formula1 = (('¬', ('p', '^', 'q')), '>', (('¬', 's'), 'v', 'r'))
formula = (('p', '^', ('¬', ('p', '>', ('¬', 'q')))), 'v', ('¬', 'q'))
atom = ['p', 'q', 'r', 's']
print('Conjunto de subfórmulas:\n', subformulas(formula, atom), '\nNumero de subformulas: ',
      len(subformulas(formula, atom)))