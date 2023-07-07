class SortedLinkedList:
    def __init__(self):
        self.linked_list = Linked_List()

    def create_sorted_linked_list(self, unsorted_list):
        bst = BST()
        bst.insert(unsorted_list[0])

        for num in unsorted_list[1:]:
            bst.insert(num)

        sorted_list = bst.in_order_traversal()

        for num in sorted_list:
            self.linked_list.append(num)

    def display(self):
        self.linked_list.display()


unsorted_list = [5, 3, 7, 2, 4, 6, 8]
sorted_linked_list = SortedLinkedList()
sorted_linked_list.create_sorted_linked_list(unsorted_list)
sorted_linked_list.display()