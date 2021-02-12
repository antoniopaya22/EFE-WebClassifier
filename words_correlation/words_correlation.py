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

def main(data):
    result = [[" " for x in range(len(list(data.keys()))+1)] for y in range(len(list(data.keys()))+1)] 
    col = 1
    for key in data:
        result[0][col] = key
        col = col+1

    row = 1
    for i in data:
        result[row][0] = i
        col = 1
        for j in data:
            spearman = stats.spearmanr(data[i], data[j])
            result[row][col] = spearman.correlation
            col = col+1
        row = row+1

    print("Correlation matrix")
    s = [[str(e) for e in row] for row in result]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

    return result
