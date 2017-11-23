import tape
import sys

class TuringMachine(object):
	
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

def main():
	print 'Conteudo Fita:', str(sys.argv[2])
	try:
		file = open(sys.argv[1], 'r')
	except IOError:
		print "Erro ao abrir o arquivo"
		return

	print 'Hello arquivo ', str(sys.argv[1])

if __name__ == "__main__":
	main()