"""
Exercise 12-1.
Write a function called most_frequent that takes a string and prints the letters in
decreasing order of frequency. Find text samples from several different languages and
see how letter frequency varies between languages
"""

with open("/home/ihor/word.txt", 'r') as file:
    data = sorted(file.read().split())
splited = []

def character():
    for char in data:
        for elem in char:
            splited.append(elem)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


if __name__ == '__main__':
    character()
    sorted_d = dict(sorted(histogram(splited).items(), key=lambda item: item[1], reverse=True))
    elems_in_total = (sum(sorted_d.values()))

    print("Total number of elements in file: ", elems_in_total)

    for key, value in sorted_d.items():
        print("Total persentage of_", key, "_is", value/elems_in_total*100, "%")