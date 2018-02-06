import nltk
import rake
import operator
class ReadDocument():

	def readFile(self,fileName):
		file = open(fileName,'r',encoding='latin1')
		fileContent = file.read()
		return fileContent

	def getKeywords(self,content):
			rake_object = rake.Rake("SmartStoplist.txt",3,2)
			keywords = rake_object.run(content)
			keywordWeights = sorted(set([word[1] for word in keywords]),reverse=True)
			requiredCount = round(0.5*len(keywordWeights))

			requiredWeights = keywordWeights[:requiredCount]

			requiredKeywords = [word[0] for word in keywords if word[1] in requiredWeights]
			return requiredKeywords

	