import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import pairwise_kernels
from csv_parser import parse_csv_amazon
from pattern.text.en import singularize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import sys


def compare_encoded_lists(list_a, list_b):
    X = np.array([list_a])
    Y = np.array([list_b])
    return pairwise_distances(X, Y, metric='manhattan')
 
def list_to_singular(l):
    new_list = []
    for element in l:
        new_list.append(singularize(element))
    return new_list

def compare_page(list_of_relevant_words, dataset, cat=None):
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
        if cat != None:
            cat_subcat = eval(categories[i])
            if cat_subcat[0] == cat:
                if comparation_val > max:
                    max = comparation_val
                    max_index = i
        else:
            if comparation_val > max:
                    max = comparation_val
                    max_index = i
    return categories[max_index]

def get_page_category(list_of_relevant_words):
    (dataset, dataset_subcat) = parse_csv_amazon()
    cat = compare_page(list_of_relevant_words, dataset)
    subcat = compare_page(list_of_relevant_words, dataset_subcat, cat)
    return cat, eval(subcat)[1]


def list_to_string(l):
    string = ''
    for elem in l:
        string = string +" "+elem
    return string

def classify_all_pages(pages):
    for page in pages.keys():
        content = list_to_string(pages[page])
        (cat, subcat) =  get_page_category([content])
        print(page)
        print("\tCategory is: ", cat)
        print("\tSubcategory is: ", subcat)


#(cat, subcat) =  get_page_category(['500 sheets standard copy paper toner ink'])
#(cat, subcat) =  get_page_category(['Samsung 960 EVO 500 GB PCIe NVMe M.2 (2280) Internal Solid State Drive (SSD) (MZ-V7S500)'])
#(cat, subcat) =  get_page_category(['Team Group 16 GB USB stick'])
#(cat, subcat) =  get_page_category(['* WINTER SALE! * Acer Aspire 5 N19H2, Intel i5 10210U Processor, 8GB RAM, 256GB SSD, 14" IPS Thin Bezel FHD Display, Windows 10, 1 Year Warranty. Packed with the latest and greatest components. Making this laptop a top performer while still being extremely energy efficient thanks to its 10th generation Intel Processor. This laptop gives you all the features you could possibly want for a daily driver machine, see specs below for more info:'+
#'Intel i5 10210U Processor 8GB DDR4 RAM, 256GB SSD, 14" IPS Thin Bezel FHD Display, Ultra Fast WIFI Connection, Long Life Battery Up To 12.5 Hours, USB Type-C x 1, USB 3.1 x 2, USB 2.0 x 1'])
data = ''
json_file = sys.argv[1]
print(json_file)
with open(json_file) as f:
  data = json.load(f)
  classify_all_pages(data)


