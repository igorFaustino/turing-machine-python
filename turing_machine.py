"""
	Script responsavel pela simulacao de uma Maquina de Turing.
"""

import tape
import copy

class TuringMachine(object):
	""" Esta classe e quem faz a simulacao. """

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
		#Acima, estao as configuracoes do que foi lido do arquivo, conforme especificado no arq. main


	def init_cabeca(self, qtd):
		"""
		Inicia um vetor de contadores para controlar a posicao na fita
			:param self: objeto TuringMachine
			:param qtd: quantidade de fitas
		"""

		cabeca = []
		for i in range(int(qtd)):
			cabeca.append(0)
		return cabeca

	def init_fita(self, conteudo_fitas, qtd, fita, simbolo_branco):
		"""
		Inicia um vetor de objetos Tape
			:param self: objeto TuringMachine
			:param conteudo_fitas: vetor de conteudo de cada fita
			:param qtd: quantidade de fitas
			:param fita: alfabeto da fita
			:param simbolo_branco: simbolo "Branco"
		"""

		fitas = []
		for i in range(int(qtd)):
			fitas.append(tape.Tape(fita, conteudo_fitas[i], simbolo_branco))
		return fitas

	def _transicao(self, tm, transicoes):
		"""
		Faz o controle entre as transicoes e o comportamento da fita
			:param self: objeto TuringMachine
			:param tm: maquina de turing
			:param transicao: transicao a ser computada
		"""

		for transicao in transicoes:
			i = transicao[3]
			tm.estado_atual = transicao[0]
			tm.fita[i].escrever(tm.cabeca[i], transicao[1])

			#transicao a direita da fita
			if transicao[2] == 'R':
				tm.cabeca[i] += 1
			#transicao a esquerda da fita
			elif transicao[2] == 'L':
				# como a funcao de escrever na fita insere elementos no comeco.. a posicao 0 sempre e o inicio da fita, logo a posicao -1 indica que a posicao lida esta fora do conteudo atual da fita
				if tm.cabeca[i] >= -1:
					tm.cabeca[i] -= 1

		if tm.estado_atual in tm.estados_finais:
			# Marca que a palavra foi aceita
			self.sucesso = True
			# retorna em cascata o conteudo atualizado das fitas
			return True, tm.fita
		else:
			# Verifica as transicoes da Maquina de Turing apos executar esta transicao e passa a diante o retorno em cascata.
			return tm._checar_transicao(tm)


	def _checar_transicao(self, tm):
		"""
		Verifica quantas transicoes sao possiveis de realizar no estado atual
		e chama a funcao _transicao para cada uma delas
			:param self: objeto TuringMachine
			:param tm: maquina de turing
		"""

		# flag para verificar se a palavra foi aceita
		_sucesso = False

		# objeto de retorno.. como a cada iteracao a mt e clonada, e necessario retornar o novo estado das fitas
		fitas = tm.fita
		for transicao in tm.transicoes:
			_transicao = []
			for i in range(int(tm.qtde_fitas)):
				if (tm.estado_atual, tm.fita[i].ler(tm.cabeca[i])) in transicao:
					_transicao.append(transicao[tm.estado_atual, tm.fita[i].ler(tm.cabeca[i])])
			if len(_transicao) == int(tm.qtde_fitas):
				_sucesso, fitas = tm._transicao(copy.deepcopy(tm), _transicao)

			if _sucesso:
				# retorna em cascata o conteudo atualizado das fitas
				return True, fitas

		# retorna em cascata o conteudo atualizado das fitas
		return False, fitas


	def executar(self):
		"""
		Executa toda a computacao das palavras
			:param self: objeto TuringMachine
		"""

		sucesso, self.fita = self._checar_transicao(self)
		self.sucesso = sucesso
		return sucesso


	def resultado(self):
		"""
		Exibe os resultados
			:param self: objeto TuringMachine
		"""

		print "\n-----------------"
		if self.sucesso:
			print "Palavra aceita"
		else:
			print "Palavra nao aceita"
		print "-----------------\n"
		
		i = 0
		for fita in self.fita:
			i = i + 1
			print "Conteudo final da fita", i, ":", fita.getConteudo()

def main():
	""" funcao principal """
	pass

if __name__ == "__main__":
	main()
