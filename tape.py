"""
	Este script serve para simular uma fita real usada na Maquina de Turing.
"""

class Tape(object):
	"""
		Class Tape: Ela quem faz a simulacao.
	"""

	def __init__(self, alfabeto="", conteudo="", simbolo_branco="B"):
		"""
		inicia a classe
			:param self: objeto Tape
			:param alfabeto="": valor da fita
		"""

		self.alfabeto = alfabeto
		self.conteudo = dict((enumerate(conteudo)))
		self.simbolo_branco = simbolo_branco

	def ler(self, posicao):
		"""
		verifica se a posicao esta na fita e retorna ela, caso o contrario informa que esta em branco
			:param self: objeto Tape
			:param posicao: posicao da cabeca
		"""

		if posicao >= 0 and posicao < len(self.conteudo):
			return self.conteudo[posicao]
		else:
			return self.simbolo_branco

	def escrever(self, posicao, valor):
		"""
		escreve os valores na fita
			:param self: objeto Tape
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
		"""
		retorna uma string com o conteudo da fita
			:param self: objeto Tape
		"""
		fita = ""
		for i  in self.conteudo:
			fita += self.conteudo[i]
		return fita


if __name__ == "__main__":
	pass
