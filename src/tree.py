import re
from src.node import Node


class Tree:
    OPERATORS = ['+', '-', '*', '/', '(', ')', '^']
    REGEX_TO_EXTRACT_NUMBERS = "-?\d*\.{0,1}\d+"

    def convert_string_to_list(self, exp):
        expression = exp
        numbers = re.findall(Tree.REGEX_TO_EXTRACT_NUMBERS, expression)
        expression = list(re.sub(Tree.REGEX_TO_EXTRACT_NUMBERS, "#", expression).replace(" ", ""))
        count = 0
        for i, c in enumerate(expression):
            if c == "#":
                expression[i] = numbers[count]
                count += 1

        return expression

    def convert_infix_to_postfix(self, exp):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        result = []

        for char in exp:
            if char == " ":
                continue
            elif not self.is_operator(char) and char.lstrip("-").isdigit():
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
        exp_list = self.convert_string_to_list(exp)
        postfix_exp = self.convert_infix_to_postfix(exp_list)
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
        # recursion
        print()
        self.print_tree(root.LeftChild)
        self.print_tree(root.RightChild)

    def evaluate(self, root):
        if root == None:
            print("Empty Tree")
            return 0

        if root.LeftChild == None and root.RightChild == None:
            return int(root.DataValue)
        # recursion
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
