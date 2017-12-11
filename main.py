# -*- coding: utf-8 -*-
"""
Universidade Tecnologica Federal do Parana - Campus Campo Mourao
Programa: Maquina de Turing Nao Deterministica com N-Fitas.
Alunos: Igor Neves Faustino, Eduardo Barbosa de Oliveira, Leticia Mazzo Portela, Jonas Felipe Alves.
Professor: Marco A. Graciotto Silva.
Curso: Bacharelado em Ciencia da Computacao.
Disciplina: Linguagens Formais Autômatos e Computabilidade.
"""

import sys
import turing_machine as TM
import util

def main():
	"""
		main function
	"""

	if len(sys.argv) < 2:
		print "modo de usar: python main.py arquivo.txt conteudo_fita1 [conteudo_fita2...]"
		return
	

	# Abrir arquivo
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

	#Das linhas 42 a 55 e feita a leitura do arquivo, conforme descrito entre as linhas 32 e 39.
	elements = []
	content = arquivo.readline() #lendo linhas 1 a 7 e associando a lista 'content'
	for i in range(7):
		#Associo o que peguei até a linha 7 à lista de 'elements'.
		elements.append(util.remove_escape_char(content))
		content = arquivo.readline()

	alfabeto_entrada = elements[0].split(' ')
	alfabeto_fita    = elements[1].split(' ')
	branco           = elements[2]
	estados          = elements[3].split(' ')
	estado_inicial   = elements[4]
	estados_finais   = elements[5].split(' ')
	qtde_fitas       = elements[6]

	#A partir da linha 58 ate a linha 64, e feita a associacao, conforme a quantidade de fitas lidas, do conteúdo delas, ficando isso armazenado na lista conteudo_fita.
	conteudo_fitas = []
	try:
		for i in range(int(qtde_fitas)):
			conteudo_fitas.append(str(sys.argv[2 + i]))
	except IndexError:
		print "modo de usar: python main.py arquivo.txt conteudo_fita1 [conteudo_fita2...]"
		return 0

	# mostrar conteudo das fitas
	for i in range(int(qtde_fitas)):
		print "conteudo da fita " + str(i+1) +":", conteudo_fitas[i]

	# A partir da linha 71 em diante, e feita a leitura das transicoes em relacao a linha 8 em diante do arquivo fornecido.
	transicoes = []
	while content:
		transicoes.append(util.remove_escape_char(content))
		content = arquivo.readline()

	# tratar transicoes
	transicoes = util.format_transicoes(transicoes, qtde_fitas)

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
							conteudo_fitas = conteudo_fitas
						)

	tm.executar()
	tm.resultado()

if __name__ == "__main__":
	main()
