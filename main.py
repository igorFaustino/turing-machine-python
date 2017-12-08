# -*- coding: utf-8 -*-
"""
					Universidade Tecnológica Federal do Paraná - Campus Campo Mourão
Programa: Máquina de Turing Não Determinística com N-Fitas.
Alunos: Igor Neves Faustino, Eduardo Barbosa de Oliveira, Letícia Mazzo Portela, Jonas Felipe Alves.
Professor: Marco A. Graciotto Silva.
Curso: Bacharelado em Ciência da Computação.
Disciplina: Linguagens Formais Autômatos e Computabilidade..
"""

"""
O projeto conta com 4 scripts: main, tape, turing_machine e util.
Além disso, conta com uma pasta intitulada testFiles, onde constam os arquivos para testar o funcionamento da Máquina de Turing.
Para executar, é necessário utilizar os seguintes comandos:
	python jflap-turing2utfpr.py nomearquivopasta.jff nomearquivopasta.txt -> Converter o arquivo
	python main.py nomearquivopasta.txt conteudo_fita1 [conteudo_fita2...conteudo_fitax]
"""

import sys
import turing_machine as TM
import util

def main():
	"""
		main function
	"""

	if len(sys.argv) < 2:
		print "Modo de usar: python main.py arquivo.txt conteudo_fita1 [conteudo_fita2... ]"
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

	#Das linhas 34 a 47 é feita a leitura do arquivo, conforme descrito entre as linhas 25 e 31.
	elements = []
	content = arquivo.readline() #Lendo linhas 1 a 7 e associando à lista 'content'.
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

	#A partir da linha 50 até a linha 56, é feita a associação, conforme a quantidade de fitas lidas, do conteúdo delas, ficando isso armazenado na lista conteudo_fita.
	conteudo_fita = []
	try:
		for i in range(int(qtde_fitas)):
			conteudo_fita.append(str(sys.argv[2+i]))
	except IndexError:
		print "modo de usar: python main.py arquivo.txt conteudo_fita1 [conteudo_fita2... ]"
		return

	# A partir da linha 63 em diante, é feita a leitura das transições em relação a linha 8 em diante do arquivo fornecido.
	transicoes = []
	while content:
		transicoes.append(util.remove_escape_char(content))
		content = arquivo.readline()

	# Tratar transições
	transicoes = util.format_transicoes(transicoes, int(qtde_fitas))
	
	# Instanciar objeto tm
	tm = TM.TuringMachine(
							alfabeto_entrada = alfabeto_entrada,
							estados          = estados,
							estado_inicial   = estado_inicial,
							estados_finais   = estados_finais,
							qtde_fitas       = qtde_fitas,
							fita             = alfabeto_fita,
							simbolo_branco   = branco,
							transicoes       = transicoes,
							conteudo_fitas   = conteudo_fita
						)

	tm.executar()
	tm.resultado()

if __name__ == "__main__":
	main()
