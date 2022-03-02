from heapq import heapify, heappop, heappush

def load_analysis_ready_text(file):
    with open(file,'r') as f:
        #skip first line
        next(f)
        text = f.read()
    return text

class HuffmanCode:
    def __init__(self, frequencies):
        self.tree = self.__create_tree(frequencies)
        self.codebook = dict()
        self.__create_codebook(self.tree, '')

    def __create_tree(self, frequencies):
        heap = [Node([s], w) for s, w in frequencies]
        heapify(heap)
        while len(heap) != 1:
            a = heappop(heap)
            b = heappop(heap)
            heappush(heap,Node([s for s in a.symbol + b.symbol], a.weight + b.weight, b, a))
        root = heap[0]
        return root

    def __create_codebook(self, node, code):
        if node.left is not None:
            self.__create_codebook(node.left, code + '1')

        if node.right is not None:
            self.__create_codebook(node.right, code + '0')

        if node.left is None and node.right is None:
            self.codebook[node.symbol[0]] = code

class Node:
    def __init__(
        self,
        symbol,
        weight,
        left = None,
        right = None,
        parent = None
    ):
        self.symbol = symbol
        self.weight = weight
        self.left = left
        if self.left is not None:
            self.left.parent = self
        self.right = right
        if self.right is not None:
            self.right.parent = self
        self.parent = parent

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'S: {self.symbol}, W: {self.weight}'
