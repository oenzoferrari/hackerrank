def levelOrder(root):
    if root is None:
        return

    """
    We enqueue the first node
    to begin the BFS
    """
    queue = [root]

    while queue:
        node = queue.pop(0)

        """
        Enqueue the nodes from left to right
        """
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        """
        Treat the last item edge case
        """
        if queue:
            print(node.info, end=" ")
        else:
            print(node.info)
