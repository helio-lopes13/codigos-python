#--Retorna o mesmo que a função seguinte
def consequencia_logica(premissas, formula):
	atom = atomicas(formula)
	for premissa in premissas:
		atom = atom.union(atomicas(premissa))
	interpretacao = {}
	return tabela_consequencia(premissas, formula, atom, interpretacao)

#--Retorna a veracidade da consequência lógica ao comparar as premissas para todas as interpretações possíveis
def tabela_consequencia(premissas, formula, atomicas, interpretacao):
	if len(atomicas) == 0:
		if valor_verdade(formula, interpretacao):
			return True
		valor_premissas = True
		for premissa in premissas:
			valor_premissas = valor_premissas and valor_verdade(premissa, interpretacao)
		if valor_premissas:
			return False
		return True

	atoms = atomicas.copy()
	atomica = atoms.pop()
	interpretacao1 = unionDict(interpretacao, {atomica: True})
	interpretacao2 = unionDict(interpretacao, {atomica: False})
	return tabela_consequencia(premissas, formula, atoms, interpretacao1) and tabela_consequencia(premissas, formula,
	                                                                                              atoms, interpretacao2)

#--Realiza uma "união" entre dois dicionários
def unionDict(dict1, dict2):
	return dict(list(dict1.items()) + list(dict2.items()))

#--Retorna a interpretação de uma fórmula A
def valor_verdade(A, verdade):
	if len(A) == 1:
		return verdade[A]
	if A[0] == '¬':
		return not valor_verdade(A[1], verdade)
	if type(A[1]) == str:
		if A[1] == '^':
			return valor_verdade(A[0], verdade) and valor_verdade(A[2], verdade)
		if A[1] == 'v':
			return valor_verdade(A[0], verdade) or valor_verdade(A[2], verdade)
		if A[1] == '>':
			if valor_verdade(A[0], verdade) == True and valor_verdade(A[2], verdade) == False:
				return False
			else:
				return True

#--Retorna o conjunto de atômicas de uma fórmula A
def atomicas(A):
	if len(A) == 1:
		return set(A)
	if A[0] == '¬':
		return atomicas(A[1])
	if type(A[1]) == str:
		return atomicas(A[0]).union(atomicas(A[2]))

#Exemplo: questão 3 da prova 1
premissas = [(('r', '^', 't'), '>', ('m', '>', ('s', 'v', 'd'))), ('j', '>', ('¬', 's')), 't', 'j', 'r', 'm']
formula = 'd'

if consequencia_logica(premissas, formula):
	print('As premissas acarretam a conclusão.')
else:
	print('As premissas não acarretam a conclusão.')