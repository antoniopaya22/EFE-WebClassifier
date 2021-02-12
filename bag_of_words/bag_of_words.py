import networkx as nx
import re

"""
Creates a list of tuples and for each word, and creates a set 
to avoid the repetitions of the edges.
"""
def obtainGraph(text):
    G = nx.Graph()
    G.add_nodes_from(text)
    edges = []
    for i in range(len(text) - 2):
        edge1 = (text[i], text[i + 1])
        edge2 = (text[i], text[i + 2])
        edge3 = (text[i + 1], text[i])
        edge4 = (text[i + 1], text[i + 2])
        edge5 = (text[i + 2], text[i])
        edge6 = (text[i + 2], text[i + 1])
        edges.append(edge1)
        edges.append(edge2)
        edges.append(edge3)
        edges.append(edge4)
        edges.append(edge5)
        edges.append(edge6)
    G.add_edges_from(set(edges))
    return G


"""
Read the first word of each line.
We obtain words that also contains the character '. 
"""


def obtainEmptyWords():
    file = open("./bag_of_words/stop.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    wordsList = []
    for line in lines:
        word = re.search(r'\w+(\')*\w*', line.split(" ", 1)[0])
        if (word): wordsList.append(word.group())

    return wordsList


def main(data, keyword_number):
    result = {}
    for key in data:
        text = re.sub("\d+", "", data[key])
        text = re.findall(r'\w+', text.lower())
        graph = obtainGraph(text)
        pr = nx.pagerank(graph)
        emptyWords = obtainEmptyWords()
        for w in emptyWords:
            if (w in pr): pr.pop(w)
        orderedWords = [k for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)]
        orderedWords = list(filter(lambda w: len(w) > 1, orderedWords))
        result[key] = orderedWords[:keyword_number]

    return result
