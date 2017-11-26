"""
	simula uma fita real usada na maquina de turing
"""

class Tape(object):
	"""
		Class Tape, simula uma fita real usada na maquina de turing
	"""

	def __init__(self, alfabeto=""):
		"""
		inicia a classe
			:param self:
			:param alfabeto="": valor da fita
		"""
		self.alfabeto = alfabeto

	def ler_fita(self, posicao):
		"""
		verifica se a posicao esta na fita e retorna ela, caso o contrario informa que esta em branco
			:param self:
			:param posicao: posicao da cabeca
		"""
		if posicao > 0 and posicao < self.alfabeto.lengh():
			return self.alfabeto[posicao]
		else:
			return False

	def escreve_fita(self, posicao, valor):
		"""
		escreve os valores na fita
			:param self: 
			:param posicao: posicao da cabeca
			:param valor: valor a ser escrito
		"""
		if posicao < 0:
			self.alfabeto = valor + self.alfabeto
		elif posicao > self.alfabeto.lengh():
			self.alfabeto = self.alfabeto + valor
		else:
			self.alfabeto[posicao] = valor


if __name__ == "__main__":
	pass
