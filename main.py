# -*- coding: utf-8 -*-
""" Main file """

import sys
import turing_machine as TM
import util

def main():
	"""
		main function
	"""

	if len(sys.argv) < 2:
		print "modo de usar: python main.py arquivo.txt conteudo_fita1 [conteudo_fita2... ]"
		return

	# abrir arquivo
	try:
		arquivo = open(sys.argv[1], 'r')
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

	#Leticia
	elements = []
	content = arquivo.readline() #lendo linhas 1 a 7 e associando à lista 'content'
	for i in range(7):
		#associo o que peguei ate a linha 7 a lista de 'elements'
		elements.append(util.remove_escape_char(content))
		content = arquivo.readline()

	alfabeto_entrada = elements[0].split(' ')
	alfabeto_fita = elements[1].split(' ')
	branco = elements[2]
	estados = elements[3].split(' ')
	estado_inicial = elements[4]
	estados_finais = elements[5].split(' ')
	qtde_fitas = elements[6]

	conteudo_fita = []
	try:
		for i in range(int(qtde_fitas)):
			conteudo_fita.append(str(sys.argv[2+i]))
	except IndexError:
		print "modo de usar: python main.py arquivo.txt conteudo_fita1 [conteudo_fita2... ]"
		return

	# for i in range(int(qtde_fitas)):
	# 	print "conteudo da fita", i+1,": ", conteudo_fita[i]


	# ler as transicoes (linha 8 em diante)
	transicoes = []
	while content:
		transicoes.append(util.remove_escape_char(content))
		content = arquivo.readline()

	# tratar transicoes
	transicoes = util.format_transicoes(transicoes, int(qtde_fitas))
	# print transicoes
	# instanciar objeto tm
	tm = TM.TuringMachine(
							alfabeto_entrada=alfabeto_entrada,
							estados=estados,
							estado_inicial=estado_inicial,
							estados_finais=estados_finais,
							qtde_fitas=qtde_fitas,
							fita=alfabeto_fita,
							simbolo_branco=branco,
							transicoes = transicoes,
							conteudo_fitas = conteudo_fita
						)

	tm.executar()
	tm.resultado()

if __name__ == "__main__":
	main()
