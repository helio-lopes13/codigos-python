# *Utilizar fórmulas na forma clausal:
# Exemplo: {frozenset({1, -2, 3}), frozenset({2, 3, -4}), frozenset({-4, 5})}
##

# Executa o DPLL recursivo definido abaixo:
def dpll(formula):
	return dpll_rec(formula, {})


# Executa o algoritmo DPLL em uma fórmula, baseado em uma valoração, de forma recursiva:
def dpll_rec(formula, valoracao):
	formula, valoracao2 = simplificar(formula)
	valoracao = union_dict(valoracao, valoracao2)
	if frozenset() in formula:
		return False
	if len(formula) == 0:
		return valoracao
	literal = get_literal(formula.copy())
	formula_copia = formula.copy()
	formula1 = formula_copia.union({frozenset({literal})})
	formula2 = formula_copia.union({frozenset({-literal})})
	res = dpll_rec(formula1, valoracao)
	if res != False:
		return res
	return dpll_rec(formula2, valoracao)


# Faz um processo chamado propagação de unidade, onde se busca cláusulas unitárias e lhes definem um valor,
# causando a remoção de cláusulas com o literal da cláusula unitaria e de seu literal complementar de outras clausulas:
def simplificar(formula):
	valoracao = {}
	while tem_unitaria(formula):
		literal_unitaria = get_literal_unitaria(formula.copy())
		if literal_unitaria < 0:
			valoracao = union_dict(valoracao, {-literal_unitaria: False})
		else:
			valoracao = union_dict(valoracao, {literal_unitaria: True})
		formula = atualizar(formula, literal_unitaria)
	return formula, valoracao


# Executa a propagação de unidade em uma formula:
def atualizar(formula, literal):
	for clausula in formula:
		if literal in clausula:
			formula = formula.difference({clausula})
		elif -literal in clausula:
			formula.remove(clausula)
			clausula_temp = set(clausula)
			clausula_temp = clausula_temp.difference({-literal})
			formula.add(frozenset(clausula_temp))
	return formula


# Verifica se uma fórmula tem clausula unitaria:
def tem_unitaria(formula):
	for clausula in formula:
		if len(clausula) == 1:
			return True
	return False


# Retorna um literal de uma clausula unitaria:
def get_literal_unitaria(formula):
	for clausula in formula:
		if len(clausula) == 1:
			clausula = set(clausula)
			return clausula.pop()


# Retorna o literal de uma clausula unitaria:
def get_literal(formula):
	for clausula in formula:
		clausula = set(clausula)
		return clausula.pop()


# Faz a união de dois dicionários:
def union_dict(dict1, dict2):
	return dict(list(dict1.items()) + list(dict2.items()))


def execucao(arquivo):
	formula = set()
	for linha in arquivo:
		linha = linha.split()
		if linha[len(linha) - 1] == '0':
			linha.remove('0')
			linha = frozenset(map(int, linha))
			formula.add(linha)
	arquivo.close()
	solucao = dpll(formula)
	if type(solucao) is dict:
		valor = ""
		for chave in solucao:
			if solucao[chave]:
				valor = valor + str(chave) + ' '
			else:
				valor = valor + str(-chave) + ' '

		valor = valor + '0'
		fim = open("solucao.cnf", "w")
		fim.write(valor)
		fim.close()
	else:
		valor = "UNSATISFIABLE"
		fim = open("solucao.cnf", "w")
		fim.write(valor)
		fim.close()


file = open("formula.cnf")
execucao(file)