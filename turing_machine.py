"""
	Simula uma maquina de turing
"""

import tape

class TuringMachine(object):
	""" Class Turing Machine, Simula uma maquina de turing """
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
		self.cabeca = 0


def main():
	""" funcao principal """
	pass

if __name__ == "__main__":
	main()
