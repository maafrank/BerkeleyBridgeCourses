 



#"""
## generator function example
## USAGE: for word in get_words(text):
##            freq_dict[word] = freq_dict.get(word, 0) +1
#common_words = ("the","be","to","of","and","a",
#                "in","that","have","i")
#
#def get_words(file):
#   """Generator function to get words from an input file"""
#   for line in file:
#      for word in line.lower().split():
#         if word not in common_words:
#            yield word.strip(string.punctuation + " ")
#"""


class MyTable(object):

    def __init__(self, length):
        self.length = length
        self.keys = [None] * self.length
        self.values = [None] * self.length

    @staticmethod
    def get_hashcode(k):
        return sum(ord(char) for char in k)
    
    @staticmethod
    def get_compression(self, hashcode):
        return hashcode % self.length

    @staticmethod
    def get_index(self, k):
        index = self.get_compression(self, self.get_hashcode(k))
        # check if index is taken
        while True:
            if self.keys[index] in [k, None]:
                break
            else:
                index += 1
                if index >= self.length: index = 0
        return index

    def __setitem__(self, k, v):
        index = self.get_index(self, k)
        self.keys[index] = k
        self. values[index] = v

    def __getitem__(self, k):
        index = self.get_index(self, k)
        if self.keys[index] == k: return self.values[index]
        else: return "Key not in table."

    def __delitem__(self, k):
        index = self.get_index(self, k)
        if self.keys[index] == k: self.keys[index] = "deleted"



m = MyTable(5)
 
# The following keys all hash to the same index.
m["a"] = "apple"
m["f"] = "butter"
m["k"] = "yummy"

print("Current keys in m:", m.keys)
print("Current values in m:", m.values)
# Current keys in m: [None, None, ’a’, ’f’, ’k’]

# "p" also hashes to the same place.
# Your class should detect that it’s not in the table
# without scanning through the entire keys list.
print("m[’p’]:", m["p"])
#m[’p’]: Key not in table.

# We can access key "k"
print("m[’k’]:", m["k"])
# Even if we remove "f"
del m["f"]
print("m[’k’]:", m["k"])
print("Current keys in m:", m.keys)
print("Current values in m:", m.values)
#m[’k’]: yummy
#m[’k’]: yummy
#Current keys in m: [None, None, ’a’, ’deleted’, ’k’]

# Even after removing "f", we can overwrite "k"
m["k"] = "newstuff"
print("Current keys in m:", m.keys)
print("Current values in m:", m.values)
#Current keys in m: [None, None, ’a’, ’deleted’, ’k’]
#Current values in m: [None, None, ’apple’, ’deleted’, ’newstuff’]
