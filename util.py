""" Funcoes uteis """

def remove_escape_char(string):
	"""
	Retira todos os caracteres especiais da string ('\n', '\r', '\t' etc)
		:param string: string a ser formatada
	"""

	escapes = ''.join([chr(char) for char in range(1, 32)])
	string = string.translate(None, escapes)
	return string

def format_transicoes(transicoes):
	"""
	Formata a string para uma lista de transicoes
		:param transicoes: transicoes a ser formatadas
	"""

	_transicao = None
	_transicoes = {}
	for transicao in transicoes:
		_transicao = transicao.split(' ')
		_transicoes[(_transicao[0], _transicao[2])] = (_transicao[1], _transicao[3], _transicao[4])

	return _transicoes
