import os
from scipy import stats

def getInitialWordsFrequency(filename):
    file = open(filename, 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    wordsList = []
    for i in range(0, 5000):
        wordsList.append(lines[i].split("\t")[0])
    return wordsList

"""
1. Obtain the list of words from both files
"""
print("Getting words from files")
scriptDirectory = os.path.dirname(__file__)
relativePath = "..\\Ejercicio1\\results.txt"
absolutePathEj1 = os.path.join(scriptDirectory, relativePath)

wordsEj1 = getInitialWordsFrequency(absolutePathEj1)
wordsEj2 = getInitialWordsFrequency("results.txt")

"""
2. Applies Spearman correlation coefficient
"""
spearman = stats.spearmanr(wordsEj1, wordsEj2)
print(spearman)
