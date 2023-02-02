from tree import Tree
import re


def main():
    # exp_tree = Tree("5711+-/3*")
    tree = Tree()
    exp_string = "((15 / (7 - (1 + 1) ) ) * -3 ) - (2 + (1 + 1))"
    print("Input String: ", exp_string)
    exp_tokens = split_in_tokens(exp_string)
    print("----------TREE------------")
    exp_tree = tree.create_tree(exp_tokens)
    tree.print_tree(exp_tree)
    print("--------Evaluation---------")
    print(tree.evaluate(exp_tree))

    '''exp_tree = tree.create_tree("( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )")
    result = tree.convert_infix_to_postfix("( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )")
    result1 = result.replace(" ", "")
    tree.print_tree(exp_tree)
    result = tree.evaluate(exp_tree)'''

    # expression = "( ( 15 / ( 7 - ( 1 + 1 ) ) ) * -3 ) - ( 2 + ( 1 + 1 ) )"
    # result = expression.split(" ")
    # print(result)

    # output = split_in_tokens(exp)

    '''expression = "((15 / (7 - (1 + 1) ) ) * -3 ) - (2 + (1 + 1))"
    numbers = re.findall('-?\d*\.{0,1}\d+', expression)
    expression = list(re.sub('-?\d*\.{0,1}\d+', "#", expression).replace(" ", ""))
    print(numbers)
    print(expression)
    count = 0
    for i, c in enumerate(expression):
        if c == "#":
            expression[i] = numbers[count]
            count += 1

    print(expression)'''

    '''postfix = tree.convert_infix_to_postfix_new(exp_list)
    print(postfix)
    print("**********")
    tree.create_tree_new(exp_list)'''


def split_in_tokens(exp):
    expression = exp
    numbers = re.findall('-?\d*\.{0,1}\d+', expression)
    expression = list(re.sub('-?\d*\.{0,1}\d+', "#", expression).replace(" ", ""))
    count = 0
    for i, c in enumerate(expression):
        if c == "#":
            expression[i] = numbers[count]
            count += 1

    return expression


if __name__ == "__main__":
    main()
