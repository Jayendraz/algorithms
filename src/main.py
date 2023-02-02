from tree import Tree


def main():
    tree = Tree()
    print("Enter input expression string: ")
    input_string = input()
    #input_string = "((15 / (7 - (1 + 1) ) ) * -3 ) - (2 + (1 + 1))"
    print("Input String: ", input_string)
    print("----------TREE------------")
    exp_tree = tree.create_tree(input_string)
    print(type(exp_tree))
    tree.print_tree(exp_tree)
    print("--------Evaluation---------")
    print(tree.evaluate(exp_tree))


if __name__ == "__main__":
    main()
