"""
	This Module simulate a turing machine
"""

import tape

class TuringMachine(object):
	"""
		Class Turing Machine, simulate a real turing machine
	"""
	def __init__(
					self,
					alfabeto_entrada = None,
					estados = [],
					estado_inicial = None,
					estados_finais = [],
					qtde_fitas = 1,
					transicoes = [],
					fita = "",
					simbolo_branco = 'B'
				):
		self.alfabeto_entrada = alfabeto_entrada
		self.estados = estados
		self.estado_inicial = estado_inicial
		self.estados_finais = estados_finais
		self.qtde_fitas = qtde_fitas
		self.transicoes = transicoes
		self.fita = tape.Tape(fita),
		self.simbolo_branco = simbolo_branco


def main():
	"""
		main function, used to test the class
	"""
	pass

if __name__ == "__main__":
	main()
