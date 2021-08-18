# W= 
# def most_frequent(string):
#     d = dict()
#     for key in string:
#         if key not in d:
#             d[key] = 1
#         else:
#             d[key] += 1
#     return d

# print (most_frequent(W))


text = input('Please enter a string ')


def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter, count)

most_frequent(text)