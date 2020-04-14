""""Trees and Graphs"""
from dataclasses import *
from typing import Any, Iterable, Optional, List


@dataclass
class Node:
    """a simple node class"""
    data: Optional[Any] = None
    children: Iterable['Node'] = field(default_factory=list)


@dataclass
class BiNode:
    """a simple node class"""
    data: Optional[Any] = None
    left: 'BiNode' = None
    right: 'BiNode' = None


@dataclass
class BiTree:
    """a simple tree class"""
    root: BiNode = BiNode()

    def in_order_traversal(self, node=root):
        """
        In-order traversal means to "visit" (often, print) the left branch,
        then the current node, and finally, the right branch.
        """
        if node:
            self.in_order_traversal(node.left)
            yield node
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node=root):
        """
        Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").
        """
        if node:
            yield node
            self.in_order_traversal(node.left)
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node=root):
        """
        Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").
        """
        if node:
            self.in_order_traversal(node.left)
            self.in_order_traversal(node.right)
            yield node


class Heap(BiTree):
    ...


class MinHeap(Heap):

    def insert(self) -> None:
        """
        When we insert into a min-heap, we always start by inserting the element at the bottom.
        We insert at the rightmost spot so as to maintain the complete tree property.

        Then, we "fix" the tree by swapping the new element with its parent,
        until we find an appropriate spot for the element. We essentially bubble up the minimum element.
        """
        pass

    def get_min(self) -> BiNode:
        """always return root"""
        return self.root

    def extract_min(self):
        """
        First, we remove the minimum element and swap it with the last element in the heap
        (the bottommost, rightmost element). Then, we bubble down this element, swapping it with one of its
        children until the min- heap property is restored.

        Do we swap it with the left child or the right child? That depends on their values.
        There's no inherent ordering between the left and right element, but you'll need to take the smaller
        one in order to maintain the min-heap ordering.
        """
        pass


class TerminatingTrieNode(Node):
    """a null node"""
    ...


@dataclass
class Trie:
    """a simple trie"""
    root: Node = Node()


@dataclass
class Queue:
    """a simple queue"""
    items: List[Any] = field(default_factory=list)

    def enqueue(self, item: Any) -> None:
        """add an item to the start of the list (end of the queue)"""
        self.items.insert(0, item)

    def dequeue(self) -> Any:
        """remove the last item in the list (start of the queue)"""
        return self.items.pop()

    def is_empty(self):
        if self.items:
            return True
        else:
            return False


@dataclass
class AdjacencyMatrix:
    """
    An adjacency matrix is an NxN boolean matrix
    (where N is the number of nodes), where a true value at matrix[i][j] means i is connected to j
    """
    matrix: List[List[bool]]


@dataclass
class GraphNode:
    """a simple graph node"""
    data: Optional[Any] = None
    visited: bool = False
    marked: bool = False
    adjacent: Iterable['GraphNode'] = field(default_factory=list)


@dataclass
class Graph:
    """a simple graph"""
    nodes: Iterable[GraphNode] = field(default_factory=list)
    root: GraphNode = GraphNode()

    def depth_first_search(self, node=root):
        """
        In depth-first search (DFS), we start at the root (or another arbitrarily selected node) and
        explore each branch completely before moving on to the next branch. That is, we go deep first
        (hence the name depth- first search) before we go wide.
        """
        if node is None:
            return
        else:
            yield node
            node.visited = True
        for n in node.adjacent:
            if n.visited:
                self.depth_first_search(n)

    @staticmethod
    def breadth_first_search(node=root):
        """
        In breadth-first search (BFS), we start at the root (or another arbitrarily selected node) and
        explore each neighbor before going on to any of their children. That is, we go wide
        (hence breadth-first search) before we go deep.
        """
        queue = Queue()
        node.marked = True
        queue.enqueue(node)

        while queue.is_empty():
            r = queue.dequeue()
            yield r
            for n in r.adjacent:
                if not n.marked:
                    n.marked = True
                    queue.enqueue(n)

    @staticmethod
    def bidirectional_search(s, t):
        """
        Two searches (one from s and one from t) that collide after four levels total (two levels each).
        """
    pass


class DiGraph(Graph):
    """a simple directed graph"""
    ...
