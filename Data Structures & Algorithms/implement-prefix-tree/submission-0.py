class TreeNode:
    def __init__(self, data: str | None, end: bool = False):
        self.data = data
        self.end = end
        self.nodes = {}


class PrefixTree:

    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = TreeNode(c)

            curr = curr.nodes[c]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.nodes:
                return False

            curr = curr.nodes[c]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.nodes:
                return False

            curr = curr.nodes[c]

        return True