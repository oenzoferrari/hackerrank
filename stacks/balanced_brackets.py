def isBalanced(s):
    pairs = {"(": ")", "[": "]", "{": "}"}

    stack = []

    for char in s:
        if char in pairs:
            stack.append(char)
            continue

        """
        If we can't match a closing pair
        with its opener, it means that the 
        str is not balanced
        """
        if not stack or char != pairs[stack[-1]]:
            return "NO"

        stack.pop()

    """ 
    If there are no unmatched openers
    the str is balanced
    """
    if len(stack) == 0:
        return "YES"

    return "NO"
