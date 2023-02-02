from node import Node


class Tree:
    OPERATORS = ['+', '-', '*', '/', '(', ')', '^']

    def convert_infix_to_postfix(self, exp):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        result = []

        for char in exp:
            if char == " ":
                continue
            if not self.is_operator(char):
                result.append(char)
            elif char == '(':
                stack.append('(')
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                    result += stack.pop()
                stack.append(char)
        while stack:
            result.append(stack.pop())

        return result

    def is_operator(self, char):
        if char in Tree.OPERATORS:
            return True
        return False

    def create_tree(self, exp):
        stack = []
        postfix_exp = self.convert_infix_to_postfix(exp)
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

        exp_tree = stack.pop()
        return exp_tree

    def print_tree(self, root):
        if root == None:
            return
        print(root.DataValue, end=": ")
        if root.LeftChild != None:
            print("L", root.LeftChild.DataValue, end=" & ")
        if root.RightChild != None:
            print("R", root.RightChild.DataValue, end=" ")
        # calling print tree recursively for all nodes in tree
        print()
        self.print_tree(root.LeftChild)
        self.print_tree(root.RightChild)

        # traverse tree and evaluate (DFS/BFS)

    def evaluate(self, root):
        if root == None:
            print("Empty Tree")
            return 0

        if root.LeftChild == None and root.RightChild == None:
            return int(root.DataValue)

        left_result = self.evaluate(root.LeftChild)
        right_result = self.evaluate(root.RightChild)

        if root.DataValue == '+':
            return left_result + right_result
        elif root.DataValue == '-':
            return left_result - right_result
        elif root.DataValue == '*':
            return left_result * right_result
        elif root.DataValue == '/':
            return left_result / right_result