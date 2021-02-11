import csv
from pattern.text.en import singularize


dataset_refinement = {}
dataset = {}
appear_counter = []

def parse_csv_amazon():

    with open('../csv_data/refinements.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #print(row)
            keywords = row[0].split(';')
            if len(keywords) > 1:
                words = []
                for i in range(1, len(keywords)):
                    words = words + keywords[i].split(' ')
                words = list(filter(lambda x: len(x) > 1, words))
                words = list(map(lambda x: singularize(x), words)) # Convert all words to singular
        
                res = [] 
                [res.append(x) for x in words if x not in res] 
                if keywords[0] not in dataset_refinement:
                    dataset_refinement[keywords[0]] = res
                else:
                    res = dataset_refinement[keywords[0]] + res
                    res2 = [] 
                    [res2.append(x) for x in res if x not in res2] 
                    dataset_refinement[keywords[0]] = res2
            

    with open('../csv_data/amazon.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            keywords = row[0].split('/')
            if len(keywords) > 1:
                words = []
                for i in range(1, len(keywords)):
                    words = words + keywords[i].split(' ')
                words = list(filter(lambda x: len(x) > 1, words))
                words = list(map(lambda x: singularize(x), words)) # Convert all words to singular

                if keywords[-1] in dataset_refinement:
                    words = words + dataset_refinement[keywords[-1]]
                res = [] 
                [res.append(x) for x in words if x not in res] 

                for elem in res:
                    if elem not in appear_counter:
                        appear_counter.append(elem)

                if keywords[1] not in dataset:
                    dataset[keywords[1]] = res
                else:
                    res = dataset[keywords[1]] + res
                    res2 = [] 
                    [res2.append(x) for x in res if x not in res2] 
                    dataset[keywords[1]] = res2

    return dataset
