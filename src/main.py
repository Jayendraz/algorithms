from tree import Tree


def main():
    #exp_tree = Tree("5711+-/3*")
    tree = Tree()
    exp_tree = tree.create_tree("((15/(7-(1+1)))*3)")
    tree.print_tree(exp_tree)


if __name__ == "__main__":
    main()