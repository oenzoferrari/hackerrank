def height(root):
    """
    The height of an empty tree
    is -1
    """
    if root is None:
        return -1

    """
    The 1+ functions as an accumulator. 
    Also in are interested only in the height
    of the tallest sub-tree
    """
    return 1 + max(height(root.left), height(root.right))
