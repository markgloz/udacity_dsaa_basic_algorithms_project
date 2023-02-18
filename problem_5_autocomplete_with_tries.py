class TrieNode:
    def __init__(self) -> None:
        self.is_word = False
        self.children = {}
        
    def insert(self, char):
        """
        Adds a child node to this trie
        """
        self.children[char] = TrieNode()
    
    def suffixes(self, suffix = ''):
        """
        Recursive function that returns all suffixes that exist in the Trie for the given prefix
        """
        suffixes = []
        char_list = [key for key in self.children.keys()]
        for s in char_list:
            if self.children[s].is_word:
                suffixes.append(suffix + s)
            suffixes.extend(self.children[s].suffixes(suffix + s))
        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Adds a word to the trie
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.insert(w)
            node = node.children[w]
        node.is_word = True

    def find(self, prefix):
        """
        Find and return the Trie node that represents the prefix.
        """
        if not prefix:
            return TrieNode()
        node = self.root
        for p in prefix:
            if p not in node.children:
                return TrieNode()
            node = node.children[p]
        return node

# Test 1 - Three words with common prefix
trie = Trie()
trie.insert('fun')
trie.insert('function')
trie.insert('factory')

prefix = 'f'
prefixNode = trie.find(prefix)
print(prefixNode.suffixes())
 # ['un', 'unction', 'actory']

# Test 2 - Multiple words with various prefixes
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

for prefix in ["a", "f", "t"]:
    prefixNode = MyTrie.find(prefix)
    print(prefixNode.suffixes())

# ['nt', 'nthology', 'ntagonist', 'ntonym']
# ['un', 'unction', 'actory']
# ['rie', 'rigger', 'rigonometry', 'ripod']

# Test 3 - Null value
prefixNode = MyTrie.find(None)
print(prefixNode.suffixes())
# []

# Test 4 - Empty value
prefixNode = MyTrie.find('')
print(prefixNode.suffixes())
# []

# Test 5 - Large value
MyTrie = Trie()
wordList = [
    "attract",
    "arise",
    "ancestor",
    "absorb",
    "album",
    "accompany",
    "announcement",
    "apathy",
    "approve",
    "adopt",
    "orientation",
    "observation",
    "operational",
    "correspondence",
    "administration",
    "responsibility",
    "discrimination",
    "recommendation",
    "infrastructure",
    "disappointment",
    "characteristic",
    "constitutional",
    "superintendent"
]
for word in wordList:
    MyTrie.insert(word)

for prefix in ["ap", "co"]:
    prefixNode = MyTrie.find(prefix)
    print(prefixNode.suffixes())

# ['athy', 'prove']
# ['rrespondence', 'nstitutional']
