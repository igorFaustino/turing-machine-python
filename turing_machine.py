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
					conteudo_fita = ''
				):
		self.alfabeto_entrada = alfabeto_entrada
		self.estados = estados
		self.estado_inicial = estado_inicial
		self.estados_finais = estados_finais
		self.qtde_fitas = qtde_fitas
		self.transicoes = transicoes
		self.fita = tape.Tape(fita, conteudo_fita)
		self.simbolo_branco = simbolo_branco
		self.cabeca = 0
		self.estado_atual = estado_inicial
		self.sucesso = False

	def _transicao(self, tm, transicao):
		"""
		Computa as transicoes da maquina de turing
			:param self:
			:param tm: maquina de turing
			:param transicao: transicao a ser computada
		"""
		simbolo_atual = tm.fita.ler(tm.cabeca)

		tm.estado_atual = transicao[0]
		tm.fita.escrever(tm.cabeca, transicao[1])

		if transicao[2] == 'R':
			tm.cabeca += 1
		elif transicao[2] == 'L':
			tm.cabeca -= 1

		if tm.estado_atual in tm.estados_finais and not (tm.estado_atual, simbolo_atual) in tm.transicoes:
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
			:param self:
			:param tm: maquina de turing
		"""
		simbolo_atual = tm.fita.ler(tm.cabeca)
		if not simbolo_atual:
			simbolo_atual = tm.simbolo_branco
		sucesso = False
		_sucesso = False
		try:
			for transicao in tm.transicoes:
				if (tm.estado_atual, simbolo_atual) in transicao:
					_sucesso = tm._transicao(copy.copy(tm), transicao[(tm.estado_atual, simbolo_atual)])

					if _sucesso:
						return True
		except KeyError:
			return False

		return sucesso


	def executar(self):
		"""
		Executa toda a computacao das palavras
			:param self:
		"""

		sucesso = self._checar_transicao(self)

		if sucesso:
			print "Linguagem aceita"
			print "fita final", self.fita.getConteudo()
		else:
			print "deu ruim"	


def main():
	""" funcao principal """
	pass

if __name__ == "__main__":
	main()
