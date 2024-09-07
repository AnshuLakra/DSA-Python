# Trie


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                node = TrieNode()
                currentNode.children.update({i: node})
            currentNode = node
        currentNode.endOfString = True
        print('inserted')

    def search(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString == True:
            return True
        else:
            return False


trie = Trie()
trie.insert("abc")
trie.insert("abcd")
print(trie.search("abcd"))
