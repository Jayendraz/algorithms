from node import Node


class Tree:
    OPERATORS = ['+', '-', '*', '/', '(', ')', '^']

    def __init__(self, exp):
        self.exp = exp

    def convert_infix_to_postfix(self):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        result = ""

        for char in self.exp:
            if not self.is_operator(char):
                result += char
            elif char == '(':
                stack.append('(')
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                    result += stack.pop()
                stack.append(char)
        while stack:
            result += stack.pop()

        return result

    def is_operator(self, char):
        if char in Tree.OPERATORS:
            return True
        return False

    def create_tree(self):
        stack = []
        postfix_exp = self.convert_infix_to_postfix()
        for item in postfix_exp:
            if self.is_operator(item):
                sub_tree_node = Node(item)
                right = stack.pop()
                left = stack.pop()
                sub_tree_node.RightChild = right
                sub_tree_node.LeftChild = left
                stack.append(sub_tree_node)
            else:
                new_node = Node(item)
                stack.append(new_node)

        expression_tree = stack.pop()

        print(expression_tree.DataValue)
        print(expression_tree.RightChild.DataValue)
        print(expression_tree.LeftChild.DataValue)
        print(expression_tree.LeftChild.LeftChild.DataValue)
        print(type(expression_tree))
        # traverse tree and evaluate (DFS/BFS)
