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

	_transicao = {}
	_transicoes = []
	for transicao in transicoes:
		transicao = transicao.split(' ')
		_transicao = { (transicao[0], transicao[2]) : (transicao[1], transicao[3], transicao[4])}
		_transicoes.append(_transicao)

	return _transicoes
