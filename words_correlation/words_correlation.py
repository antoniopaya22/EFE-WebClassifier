from scipy import stats


def getInitialWordsFrequency(filename):
    file = open(filename, 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    wordsList = []
    for i in range(0, 5000):
        wordsList.append(lines[i].split("\t")[0])
    return wordsList


def check_if_len_less_than(arr_a, keyword_number):
    if len(arr_a) < keyword_number:
        for i in range(len(arr_a), 20):
            arr_a.append('')
    return arr_a


def main(data, keyword_number):
    result = [[" " for x in range(len(list(data.keys())) + 1)] for y in range(len(list(data.keys())) + 1)]
    col = 1
    for key in data:
        result[0][col] = key
        col = col + 1

    row = 1
    for i in data:
        result[row][0] = i
        col = 1
        arr_a = check_if_len_less_than(data[i], keyword_number)
        for j in data:
            arr_b = check_if_len_less_than(data[j], keyword_number)
            spearman = stats.spearmanr(arr_a, arr_b)
            result[row][col] = spearman.correlation
            col = col + 1
        row = row + 1

    # s = [[str(e) for e in row] for row in result]
    # lens = [max(map(len, col)) for col in zip(*s)]
    # fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    # table = [fmt.format(*row) for row in s]
    # print('\n'.join(table))

    return result
