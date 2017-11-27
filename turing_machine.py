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

	def transicao(self):
		simbolo_atual = self.fita.ler(self.cabeca)

		if not simbolo_atual:
			simbolo_atual = self.simbolo_branco

		try:
			transicao = self.transicoes[(self.estado_atual, simbolo_atual)]
		except KeyError:
			return False

		self.estado_atual = transicao[0]
		self.fita.escrever(self.cabeca, transicao[1])

		if transicao[2] == 'R':
			self.cabeca += 1
		elif transicao[2] == 'L':
			self.cabeca -= 1
		
		return True

	def executar(self):
		sucesso = True
		while self.estado_atual not in self.estados_finais and sucesso:
			sucesso = self.transicao()
		
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
