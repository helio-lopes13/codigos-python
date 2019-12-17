#*Utilizar fórmulas na forma clausal:
#Exemplo: {frozenset({1, -2, 3}), frozenset({2, 3, -4}), frozenset({-4, 5})}
##

#Executa o DPLL recursivo definido abaixo:
def dpll(formula):
	return dpll_rec(formula, {})


def dpll_rec(formula, valoracao):
	formula, valoracao2 = simplificar(formula)
	valoracao = union_dict(valoracao, valoracao2)
	if frozenset() in formula:
		return False
	if len(formula) == 0:
		return valoracao
	literal = get_literal(formula)
	formula_copia = formula.copy()
	formula1 = formula_copia.union({frozenset({literal})})
	formula2 = formula_copia.union({frozenset({-literal})})
	res = dpll_rec(formula1, valoracao)
	if res != False:
		return res
	return dpll_rec(formula2, valoracao)


def simplificar(formula):
	valoracao = {}
	while tem_unitaria(formula):
		literalUnitaria = get_literal_unitaria(formula.copy())
		if literalUnitaria < 0:
			valoracao = union_dict(valoracao, {-literalUnitaria: False})
		else:
			valoracao = union_dict(valoracao, {literalUnitaria: True})
		formula = atualizar(formula, literalUnitaria)
	return formula, valoracao


def atualizar(formula, literal):
	for clausula in formula:
		if literal in clausula:
			formula = formula.difference({clausula})
		elif -literal in clausula:
			formula.remove(clausula)
			clausulaTemp = set(clausula)
			clausulaTemp = clausulaTemp.difference({-literal})
			formula.add(frozenset(clausulaTemp))
	return formula


def tem_unitaria(formula):
	for clausula in formula:
		if len(clausula) == 1:
			return True
	return False


def get_literal_unitaria(formula):
	for clausula in formula:
		if len(clausula) == 1:
			for literal in clausula:
				return literal


def get_literal(formula):
	for clausula in formula:
		for literal in clausula:
			return literal


def union_dict(dict1, dict2):
	return dict(list(dict1.items()) + list(dict2.items()))


formula = {frozenset({-1, -2}), frozenset({-1, 2})}
solucao = dpll(formula)
if type(solucao) is dict:
	print('A valoração que satisfaz a fórmula é: ', solucao)
else:
	print('A fórmula é insatisfazível.')

