# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    
    # This example modifies my_list, which is not necessary, but it still works.
    # if len(my_list) == 0:
    #     return

    # print my_list.pop(i)
    # print_item(my_list, i=0)

    if i < len(my_list):
        print my_list[i]
        i +=1
        print_item(my_list, i)


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    print tree.data
    if tree.children == []:
        return
    
    children = (tree.children)
    for child in children:
        print_all_tree_data(child)

    # This option doesn't have an explicit base case, but it still works.
    # print tree.data
    # children = (tree.children)
    # for child in children:
    #     print_all_tree_data(child)


# 3. Write a function that uses recursion to find the length of a list.

def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    # This function adjusts the list, which isn't necessary for the problem.
    # if my_list == []:
    #     return 0

    # my_list.pop(-1)
    # return 1 + list_length(my_list)


    # This function binds an identifier to an adjustment of a list, which isn't necessary... 
    # if my_list == []:
    #     return 0

    # my_new_list = my_list[1:]
    # return 1 + list_length(my_new_list)

    if my_list == []:
        return 0

    return 1 + list_length(my_list[1:])



# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    pass

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
