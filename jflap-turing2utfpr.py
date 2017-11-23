#    Linha 1: alfabeto de entrada
#    Linha 2: alfabeto da fita
#    Linha 3: simbolo que representa um espaco em branco na fita
#    Linha 4: estado inicial
#    Linha 5, coloquem uma linha indicando o conjunto de estados de aceitacao
#    Linhas 6 em diante: transicoes, uma por linha, no formato estado atual, simbolo atual,  novo estado, novo simbolo, direcao para mover a cabeca

from xml.etree import ElementTree as ET
import csv
import sys

class Transition(object):
	def __init__(self):
		self.currentState = None
		self.newState = None
		self.tapeMovements = []

class TapeMovement(object):
	def __init__(self):
		self.tape = 1
		self.currentTapeSymbol = None
		self.newTapeSymbol = None
		self.headDirection = None


class Jflap2Utfpr(object):
	def __init__(self):
		self.alphabet = set()
		self.states = set()
		self.tapeSymbols = set()
		self.tapes = 1
		self.initialState = None
		self.finalStates = set()
		self.transitions = set()

	def convert(self, inputFile, outputFile, blankSymbol = 'B', alphabet = None):
		if alphabet is None:
			self.alphabet = self.tapeSymbols
		else:
			self.alphabet = alphabet

		self.blankSymbol = blankSymbol
		self.tapeSymbols.add(blankSymbol)

		xmldoc = ET.parse(inputFile)
		root = xmldoc.getroot()
		self.tapes = int(root.find('tapes').text)

		tm = root.find('automaton')
		for s in tm.findall('block'):
			state = s.attrib['id']
			self.states.add(state)
			if s.find('initial') is not None:
				self.initialState = state
			if s.find('final') is not None:
				self.finalStates.add(state)

		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.add(transition)
			transition.currentState = t.find('from').text
			transition.newState = t.find('to').text
			for i in range(1, self.tapes+1):
				movement = TapeMovement()
				transition.tapeMovements.append(movement)
				movement.tape = i
				if t.find("read[@tape='" + str(i) + "']").text is not None:
					movement.currentTapeSymbol = t.find("read[@tape='" + str(i) + "']").text
					self.tapeSymbols.add(movement.currentTapeSymbol)
				else:
					movement.currentTapeSymbol = blankSymbol
				if t.find("write[@tape='" + str(i) + "']").text is not None:
					movement.newTapeSymbol = t.find("write[@tape='" + str(i) + "']").text
					self.tapeSymbols.add(movement.newTapeSymbol)
				else:
					movement.newTapeSymbol = blankSymbol
				movement.headDirection = t.find("move[@tape='" + str(i) + "']").text
		
		with open(outputFile, 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=' ')
			writer.writerow(list(self.alphabet))
			writer.writerow(list(self.tapeSymbols))
			writer.writerow([self.blankSymbol])
			writer.writerow(self.initialState)
			writer.writerow(list(self.finalStates))
			writer.writerow([self.tapes])
			for transition in self.transitions:
				transitionDescription = []
				transitionDescription.append(transition.currentState)
				transitionDescription.append(transition.newState)
				for i in range(1, self.tapes+1):
					for movement in transition.tapeMovements:
						if movement.tape == i:
							transitionDescription.append(movement.currentTapeSymbol)
							transitionDescription.append(movement.newTapeSymbol)
							transitionDescription.append(movement.headDirection)
				writer.writerow(transitionDescription)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
		sys.exit(1)
	converter = Jflap2Utfpr()
	converter.convert(sys.argv[1], sys.argv[2])
