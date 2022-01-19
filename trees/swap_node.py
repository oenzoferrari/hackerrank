from sys import setrecursionlimit
from collections import deque


# Problem exceeds python default recursion limit
setrecursionlimit(10000)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(indexes):
    root = Node(1)

    """
    The deque is a double ended queue,
    faster for append and popping from
    both sides
    """
    queue = deque([root])

    """
    Populates the queue in a BFS way.
    the indexes format is [[a, b], [c, d], [e, f]]...
    
    so:
                  1
            a           b
          c    d     e     f 
    """
    for left, right in indexes:
        current_node = queue.popleft()

        if left != -1:
            node = Node(left)
            current_node.left = node

            queue.append(node)

        if right != -1:
            node = Node(right)
            current_node.right = node

            queue.append(node)

    return root


def swap(root, swap_depth, current_depth, result_list):
    if root is None:
        return

    # If the depth is a multiple of the swap_depth, swap
    if current_depth % swap_depth == 0:
        root.left, root.right = root.right, root.left

    """ 
    Swap the subtrees in-order
    """
    swap(root.left, swap_depth, current_depth + 1, result_list)
    result_list.append(root.val)
    swap(root.right, swap_depth, current_depth + 1, result_list)


def swapNodes(indexes, queries):
    root = buildTree(indexes)

    results = []
    for k in queries:
        swap_result = []
        swap(root, swap_depth=k, current_depth=1, result_list=swap_result)

        results.append(swap_result)

    return results
