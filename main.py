""" Main file """

import sys
import turing_machine as TM

def main():
	"""
		main function
	"""

	conteudo_fita = str(sys.argv[2])
	print "conteudo da fita:", conteudo_fita

	# abrir arquivo
	try:
		file = open(sys.argv[1], 'r')
	except IOError:
		print "Erro ao abrir o arquivo"
		return

	# Ler as linhas do arquivo (linha 1 a 7)
		# Linha 1: alfabeto de entrada
		# Linha 2: alfabeto da fita
		# Linha 3: simbolo que representa o espaco em branco (padrao: B)
		# Lista 4: conjunto de estados
		# Linha 5: estado inicial
		# Linha 6: conjunto de estados finais
		# Linha 7: quantidade de fitas

	# ler as transicoes (linha 8 em diante)

	# tratar transicoes

	# instanciar objeto tm
	tm = TM.TuringMachine()

	print 'Hello arquivo ', str(sys.argv[1])
