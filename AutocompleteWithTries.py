# Represents a single node in the Trie
class TrieNode:

    # Initialize this node in the Trie
    def __init__(self):
        self.children = dict()
        self.is_word = False

    # Add a child node in this Trie
    def insert(self, char):

        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):

        result = self.suffixes_recursive(suffix, list())
        return result

    def suffixes_recursive(self, sequence, result):

        for char in self.children:
            cur_node = self.children[char]
            if cur_node.is_word:
                result.append(sequence + char)
            result = cur_node.suffixes_recursive(sequence + char, result)

        return result


# The Trie itself containing the root node and insert/find functions
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Add a word to the Trie
    def insert(self, word):

        self.root.insert(word[0])
        cur_trie_node = self.root.children[word[0]]
        for i in range(1, len(word)):
            cur_trie_node.insert(word[i])
            cur_trie_node = cur_trie_node.children[word[i]]

        cur_trie_node.is_word = True

    # Find the Trie node that represents this prefix
    def find(self, prefix):

        if prefix in self.root.children:
            return self.root.children[prefix]

        for key in self.root.children:
            if prefix == key:
                return self.root.children[key]

        return None


MyTrie = Trie()

prefix_test = 'a'
if MyTrie.find(prefix_test):
    print('"{}" prefix found'.format(prefix_test))
    prefixNode = MyTrie.find(prefix_test)
    print('\n'.join(prefixNode.suffixes()))
else:
    print('"{}" not found.'.format(prefix_test))


# wordList = [
#     "ant", "anti", "ander", "andir", "an", "amazing", "anolastletter"
# ]

wordList = [
     "ant", "anthology", "antagonist", "antonym",
     "fun", "function", "factory", "good",
     "trie", "trigger", "trigonometry", "tripod",
     "anti", "ander", "andir", "an", "amazing", "anolastletter"
]

for pword in wordList:
    MyTrie.insert(pword)

# print(MyTrie)

#test_words = ['a']
test_prefixes = ['aa', 'a', 't', 'f', 'g', 'k', 'j']

for prefix_test in test_prefixes:
    if MyTrie.find(prefix_test):
        print('"{}" prefix found'.format(prefix_test))
        prefixNode = MyTrie.find(prefix_test)
        print('\n'.join(prefixNode.suffixes()))
    else:
        print('"{}" not found.'.format(prefix_test))

