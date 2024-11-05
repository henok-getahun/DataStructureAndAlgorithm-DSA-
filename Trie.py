class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        #nserts a word into the Trie
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def search(self, word):
        #Searches for a word in the Trie
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

    def remove(self, word):
        #Removes a word from the Trie
        current = self.root
        stack = []

        for char in word:
            if char not in current.children:
                raise ValueError("Word not found")
            stack.append((current, char))
            current = current.children[char]

        current.end_of_word = False

        # Remove nodes if they are no longer needed
        for parent, char in reversed(stack):
            if not current.children and not current.end_of_word:
                del parent.children[char]
                current = parent
            else:
                break

    def starts_with(self, prefix):
      #Returns True if there is any word in the Trie that starts with the given prefix.
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


    trie = Trie()
    trie.add_word("hello")
    trie.add_word("helium")

    print(trie.search("hello"))  # Output: True
    print(trie.search("hel"))     # Output: False
    print(trie.starts_with("hel")) # Output: True

    trie.remove("hello")
    print(trie.search("hello"))  # Output: False
