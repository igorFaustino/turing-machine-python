def remove_escape_char(string):
	"""
	Retira todos os caracteres especiais da string ('\n', '\r', '\t' etc)
		:param string: string a ser formatada
	"""

	escapes = ''.join([chr(char) for char in range(1, 32)])
	string = string.translate(None, escapes)
	return string

def format_transicoes(transicoes, qtd):
	"""
	Formata a string para uma lista de transicoes
		:param transicoes: transicoes a serem formatadas
	"""

	_transicoes = []
	for transicao in transicoes:
		_transicao = {}
		transicao = transicao.split(' ')
		for i in range(int(qtd)):
			_transicao[(transicao[0], transicao[2 + i*3])] = (transicao[1], transicao[3 + i*3], transicao[4 + i*3], i)

		_transicoes.append(_transicao)

	return _transicoes
