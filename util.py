""" Funções úteis """

def remove_escape_char(string):
	"""
	Retira todos os caracteres especiais da string ('\n', '\r', '\t' etc)
		:param string: string a ser formatada
	"""

	escapes = ''.join([chr(char) for char in range(1, 32)])
	string = string.translate(None, escapes)
	return string

def format_transicoes(transicoes, qtd_fitas):
	"""
	Formata a string para uma lista de transições
		:param transicoes: transições a serem formatadas
	"""
	qtd_fitas = int(qtd_fitas)
	_transicoes = []
	for transicao in transicoes:
		_transicao = {}
		transicao = transicao.split(' ')
		for i in range(qtd_fitas):
			_transicao[(transicao[0], transicao[2 + (i*3)])] = (transicao[1], transicao[3 + (i*3)], transicao[4 + (i*3)], i)
		_transicoes.append(_transicao)

	return _transicoes
