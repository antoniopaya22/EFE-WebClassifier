import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import pairwise_kernels
from csv_parser import parse_csv_amazon
from pattern.text.en import singularize
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity


def compare_encoded_lists(list_a, list_b):
    X = np.array([list_a])
    Y = np.array([list_b])
    return pairwise_distances(X, Y, metric='manhattan')
 
def list_to_singular(l):
    new_list = []
    for element in l:
        new_list.append(singularize(element))
    return new_list

def compare_page(list_of_relevant_words):
    dataset= parse_csv_amazon()
    categories = list(dataset.keys())
    seq = list(dataset.values())
    full_list = []
    for l in seq:
        word = ''
        for w in l:
            word = word + " " + w
        full_list.append(word)
    list_of_relevant_words = list_to_singular(list_of_relevant_words)
    # Text feature extraction
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(full_list)
    amazon_list = X.toarray()

    page = vectorizer.transform(list_of_relevant_words).toarray() 
    # Comparation
    max = 0
    max_index = -1
    for i in range(0, len(amazon_list)):
        comparation_val = cosine_similarity(amazon_list[i].reshape(1, -1), page[0].reshape(1, -1))
        print(comparation_val)
        if comparation_val > max:
            max = comparation_val
            max_index = i
    print(categories)
    return categories[max_index]

def get_page_category(list_of_relevant_words):
    return compare_page(list_of_relevant_words)


print("Category is: ", get_page_category(['500 sheets standard copy paper']))
