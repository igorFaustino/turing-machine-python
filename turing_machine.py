"""
	Simula uma maquina de turing
"""

import tape
import copy

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
					fita = None,
					simbolo_branco = 'B',
					conteudo_fitas = []
				):
		self.alfabeto_entrada = alfabeto_entrada
		self.estados = estados
		self.estado_inicial = estado_inicial
		self.estados_finais = estados_finais
		self.qtde_fitas = qtde_fitas
		self.transicoes = transicoes
		self.fita = self.init_fita(conteudo_fitas, qtde_fitas, fita, simbolo_branco)
		self.simbolo_branco = simbolo_branco
		self.cabeca = self.init_cabeca(qtde_fitas)
		self.estado_atual = estado_inicial
		self.sucesso = False

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
		Computa as transicoes da maquina de turing
			:param tm: maquina de turing
			:param transicao: transicao a ser computada
		"""

		tm.estado_atual = transicoes[0][0]
		for transicao in transicoes:
			i = transicao[3]
			tm.fita[i].escrever(tm.cabeca[i], transicao[1])

			if transicao[2] == 'R':
				tm.cabeca[i] += 1
			elif transicao[2] == 'L':
				tm.cabeca[i] -= 1

		if tm.estado_atual in tm.estados_finais:
			# marca que a palavra foi aceita
			self.sucesso = True
			return True
		else:
			# verifica as transicoes da maquina de turing apos executar esta transicao
			return tm._checar_transicao(tm)


	def _checar_transicao(self, tm):
		"""
		Verifica quantas transicoes sao possiveis de realizar no estado atual
		e chama a funcao _transicao para cada uma delas
			:param tm: maquina de turing
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
		Executa toda a computacao das palavras
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
