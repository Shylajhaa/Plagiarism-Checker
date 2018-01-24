import nltk
class ReadDocument():
	def printFile(self,fileName):
		required = ['CD', 'FW', 'LS', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'RP','JJ']
		file = open(fileName,'r',encoding='latin1')
		fileContent = file.read()
		#print(type(fileContent))
		text = nltk.word_tokenize(fileContent)
		tags = nltk.pos_tag(text)
		#for x in tags:
		#	print(x)
		keywords = []
		for tag,part in tags:
			if part in required:
				keywords.append(tag)
		#for x in keywords:
		#	print(x)
		print(fileName+" "+str(len(set(keywords))))


fileName1 = 'holography.txt'
fileName2 = 'RaspberryPiabsoly.txt'
fileName3 = 'virtualMouse.txt'
fileName4 = 'nanorobots.txt'
fileName5 = 'miniSearchEngine.txt'
fileName6 = 'password.txt'
obj = ReadDocument()
obj.printFile(fileName1)
obj.printFile(fileName2)
obj.printFile(fileName3)
obj.printFile(fileName4)
obj.printFile(fileName5)
obj.printFile(fileName6)