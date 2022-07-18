from typing import List
import numpy as np

class ListNode:
    def __init__(self, val: int, next: any) -> None:
        """
        Creates a ListNode which is a node of a singly linked list. 

        @param: val: int, next: ListNode | None
        @property: self.val: int, self.next: ListNode | None
        """ 
        self.val = val
        self.next = next

def copy_list(head: ListNode) -> ListNode:
    """
    Helper function, that copies a complete list. Used inside a 
    function to prevent altering lists passed in as arguments.
    
    @param: head: ListNode | None
    @property: ListNode | None
    """ 

    if not head:
        return None

    res = ptr = ListNode(head.val, None)
    head = head.next

    while head:
        ptr.next = ListNode(head.val, None)
        ptr = ptr.next
        head = head.next

    return res

def print_list(head: ListNode):
    """
    Takes in a ListNode *head* and prints values of all ListNodes starting with *head*

    @param: head: ListNode | None
    @return: None
    """
    head = copy_list(head)

    while(head):
        print(str(head.val))
        head = head.next

def create_random_ordered_list() -> ListNode:
    """
    Creates and returns a List with random length and random values in ascending order
    list_length is in [0, 100]. Values are within [low_bnd, low_bnd + 5] where low_bnd initially is within [0, 5]
    and is set to the last value with every new ListNode.

    @param: None
    @return: ListNode | None
    """ 
    length = int(np.random.randint([0], 100))

    if not length:
        return None

    low_bnd = int(np.random.randint([0], 5))
    tmp = ListNode(low_bnd, None)
    head = tmp

    for i in range(0, length):
        low_bnd = int(np.random.randint([low_bnd], low_bnd+5))
        tmp.next = ListNode(low_bnd, None)
        tmp = tmp.next

    return head        

def check_if_list_sorted(list: ListNode) -> bool:
    """
    Helper function that takes in a ListNode *list* and checks whether the List is in ascending order.
    Returns False if *list* is None

    @param: head: ListNode | None
    @return: bool
    """ 
    list = copy_list(list)

    if not list:
        return False

    prev = list.val
    list = list.next
    while(list):
        if list.val < prev:
            return False
        prev = list.val
        list = list.next

    return True

def check_if_list_is_union(list1: ListNode, list2: ListNode, union: ListNode) -> bool:
    """
    Helper function that takes in three lists and checks wheter the third list is a union of the first and second list. 
    A list is a union of two lists, if it contains exactly the values the two lists contain. If a value is contained n times in 
    the two lists together, its also contained n times in the union. The order of the values doesn't matter. 
    Returns True if it is a union, False otherwise.

    @param: list1: ListNode | None, list2: ListNode | None, union: ListNode | None
    @return: bool
    """ 
    list1 = copy_list(list1)
    list2 = copy_list(list2)
    union = copy_list(union)

    seen = {}
    
    while list1:
        if list1.val in seen:
            seen[list1.val] += 1
        else:
            seen[list1.val] = 1
        list1 = list1.next

    while list2:
        if list2.val in seen:
            seen[list2.val] += 1
        else:
            seen[list2.val] = 1
        list2 = list2.next

    while union:
        if union.val in seen:
            seen[union.val] -= 1
            union = union.next
        else:
            return False
    
    for key in seen:
        if seen[key] != 0:
            return False
        
    return True
