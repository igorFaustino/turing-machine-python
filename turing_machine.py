"""
	Script responsável pela simulação de uma Máquina de Turing.
"""

import tape
import copy

class TuringMachine(object):
	""" Esta classe é quem faz a simulação. """

	def __init__(
					self,
					alfabeto_entrada = None,
					estados          = [],
					estado_inicial   = None,
					estados_finais   = [],
					qtde_fitas       = 1,
					transicoes       = [],
					fita             = None,
					simbolo_branco   = 'B',
					conteudo_fitas   = []
				):
		self.alfabeto_entrada = alfabeto_entrada
		self.estados          = estados
		self.estado_inicial   = estado_inicial
		self.estados_finais   = estados_finais
		self.qtde_fitas       = qtde_fitas
		self.transicoes       = transicoes
		self.fita             = self.init_fita(conteudo_fitas, qtde_fitas, fita, simbolo_branco)
		self.simbolo_branco   = simbolo_branco
		self.cabeca           = self.init_cabeca(qtde_fitas)
		self.estado_atual     = estado_inicial
		self.sucesso          = False
		#Acima, estão as configurações do que foi lido do arquivo, conforme especificado no arq. main

	def init_cabeca(self, qtd):
		cabeca = []
		for i in range(int(qtd)):
			cabeca.append(0)
		return cabeca

	def init_fita(self, conteudo_fitas, qtd, fita, simbolo_branco):
		fitas = []
		for i in range(int(qtd)):
			fitas.append(
				tape.Tape(fita, conteudo_fitas[i], simbolo_branco)
			)
		return fitas

	def _transicao(self, tm, transicoes):
		"""
		Computa as transições da Máquina de Turing
			:param tm: Máquina de Turing
			:param transicao: transição a ser computada
		"""
		""" Faz o controle entre as transições e o comportamento da fita """
		tm.estado_atual = transicoes[0][0]
		for transicao in transicoes:
			i = transicao[3]
			tm.fita[i].escrever(tm.cabeca[i], transicao[1])

			if transicao[2] == 'R': #transiçao a direita da fita
				tm.cabeca[i] += 1
			elif transicao[2] == 'L': #transição a esquerda da fita
				tm.cabeca[i] -= 1

		if tm.estado_atual in tm.estados_finais:
			# Marca que a palavra foi aceita
			self.sucesso = True
			return True
		else:
			# Verifica as transições da Máquina de Turing após executar esta transição.
			return tm._checar_transicao(tm)


	def _checar_transicao(self, tm):
		"""
		Verifica quantas transições são possíveis de realizar no estado atual
		e chama a funcao _transicao para cada uma delas
			:param tm: Máquina de Turing
		"""

		_sucesso = False
		_transicao = []
		try:
			for transicao in tm.transicoes:
				cont_fitas = 0
				for i in range(int(tm.qtde_fitas)):
					if (tm.estado_atual, tm.fita[i].ler(tm.cabeca[i])) in transicao:
						cont_fitas = cont_fitas + 1
						_transicao.append(transicao[(tm.estado_atual, tm.fita[i].ler(tm.cabeca[i]))])
				if cont_fitas == int(self.qtde_fitas):
					_sucesso = tm._transicao(copy.copy(tm), _transicao)
					_transicao = []
		except KeyError:
			return False

		return _sucesso


	def executar(self):
		"""
		Executa toda a computação das palavras
		"""

		sucesso = self._checar_transicao(self)
		self.sucesso = sucesso
		return sucesso

	def resultado(self):
		"""
		Exibe os resultados
		"""
		if self.sucesso:
			print "Linguagem aceita"
			i = 0
			for fita in self.fita:
				i = i + 1
				print "Conteudo final da fita", i, ":", fita.getConteudo()
		else:
			print "Linguagem nao aceita"

def main():
	""" funcao principal """
	pass

if __name__ == "__main__":
	main()
