from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from ReadDocument import ReadDocument
import spacy

class Similarity():
	nlp = spacy.load('en_vectors_web_lg')
	stop_words = set(stopwords.words('english'))

	'''fileName1 = 'holography.txt'
	fileName2 = 'RaspberryPiabsoly.txt'
	fileName3 = 'virtualMouse.txt'
	fileName4 = 'nanorobots.txt'
	fileName5 = 'miniSearchEngine.txt'
	fileName6 = 'password.txt'

	def readFile(fileName):
		file = open(fileName,'r',encoding='latin1')
		fileContent = file.read()
		return fileContent'''


	def toString(self,listName):
		value = ""
		count = 0
		for word in listName:
			value = value + word + " "
			#count = count + 1
			#if(count%100 == 0):
				#print(str(count)+" words done")
		return value


	def removeStopwords(self,content):
		sim = Similarity()
		stop_words = set(stopwords.words('english'))
		#print("Stop words loaded")
		words = content.split(' ')
		#print("String split into words")
		fileWithoutStopWords = [word for word in words if word not in stop_words]
		#print("list with no stopwords")
		contentWithoutStopWords = sim.toString(fileWithoutStopWords)
		#print("list to string converted")
		return contentWithoutStopWords


	def findMeasure(self,string1,string2):
		nlp = spacy.load('en_vectors_web_lg')
		listOfSentences1 = string1.split('.')
		listOfSentences2 = string2.split('.')
		#print("Split into sentenes")
		measures  = []
		for line1 in listOfSentences1:
			for line2 in listOfSentences2:
				doc1 = nlp(line1)
				doc2 = nlp(line2)
				measures.append(doc1.similarity(doc2))
		count = len(measures)
		sim = 0
		for value in measures:
			if(value>0.75):
				sim = sim + 1
		return sim/count

	def stemWords(self,document):
		stemmer = PorterStemmer()
		docList = document.split(' ')
		stemmedDoc  = ""
		for word in docList:
			stemmedDoc = stemmedDoc + " " + stemmer.stem(word)
		return stemmedDoc


	def similarValue(self,file1,file2):
		readDoc = ReadDocument()
		sim = Similarity()
		fileContent1 = readDoc.readFile(file1)
		fileContent2 = readDoc.readFile(file2)
		#print("File reading done")
		file1WithoutStopWords = sim.removeStopwords(fileContent1)
		#print("Stop words in file1 removed")
		file2WithoutStopWords = sim.removeStopwords(fileContent2)
		#print("Stop Words in file2 removed")
		file1AfterStemming = sim.stemWords(file1WithoutStopWords)
		file2AfterStemming = sim.stemWords(file2WithoutStopWords)

		#print(file1AfterStemming)
		#print(file2AfterStemming)

		similarityValue = sim.findMeasure(file1AfterStemming,file2AfterStemming)
		return similarityValue


