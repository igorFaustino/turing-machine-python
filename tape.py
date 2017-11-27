"""
	simula uma fita real usada na maquina de turing
"""

class Tape(object):
	"""
		Class Tape, simula uma fita real usada na maquina de turing
	"""

	def __init__(self, alfabeto="",conteudo=""):
		"""
		inicia a classe
			:param self:
			:param alfabeto="": valor da fita
		"""
		self.alfabeto = alfabeto
		self.conteudo = dict((enumerate(conteudo)))

	def ler(self, posicao):
		"""
		verifica se a posicao esta na fita e retorna ela, caso o contrario informa que esta em branco
			:param self:
			:param posicao: posicao da cabeca
		"""
		if posicao >= 0 and posicao < len(self.conteudo):
			return self.conteudo[posicao]
		else:
			return False

	def escrever(self, posicao, valor):
		"""
		escreve os valores na fita
			:param self:
			:param posicao: posicao da cabeca
			:param valor: valor a ser escrito
		"""
		if posicao < 0:
			fita = ""
			for i  in self.conteudo:
				fita += self.conteudo[i]
			fita = valor + fita
			self.conteudo = dict((enumerate(fita)))

		elif posicao > len(self.conteudo):
			fita = ""
			for i  in self.conteudo:
				fita += self.conteudo[i]
			fita = fita + valor
			self.conteudo = dict((enumerate(fita)))
		else:
			self.conteudo[posicao] = valor

	def getConteudo(self):
		fita = ""
		for i  in self.conteudo:
			fita += self.conteudo[i]
		return fita


if __name__ == "__main__":
	pass
