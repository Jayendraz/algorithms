from tree import Tree


def main():
    #exp_tree = Tree("5711+-/3*")
    tree = Tree()
    exp_tree = tree.create_tree("((5/(7-(1+1)))*3)-(2+(1+1))")
    tree.print_tree(exp_tree)
    result = tree.evaluate(exp_tree)
    print(result)


if __name__ == "__main__":
    main()
