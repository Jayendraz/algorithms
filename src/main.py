from tree import Tree


def main():
    #exp_tree = Tree("5711+-/3*")
    exp_tree = Tree("((15/(7-(1+1)))*3)")
    exp_tree.create_tree()


if __name__ == "__main__":
    main()