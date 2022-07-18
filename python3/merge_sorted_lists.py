from typing import List
from ListHelpers.ListHelpers import ListNode, print_list, create_random_ordered_list, check_if_list_sorted, check_if_list_is_union, copy_list

def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    list1 = copy_list(list1)
    list2 = copy_list(list2)

    tail = res = ListNode(-1, None)

    while True:
        if list1 is None:
            tail.next = list2
            break
        if list2 is None:
            tail.next = list1
            break

        if list1.val <= list2.val:
            tail.next = ListNode(list1.val, None)
            list1 = list1.next
        else:
            tail.next = ListNode(list2.val, None)
            list2 = list2.next

        tail = tail.next

    return res.next

def main() -> None:
    l1 = create_random_ordered_list()
    l2 = create_random_ordered_list()
    print("List1:")
    print_list(l1)
    print("")
    print("List2:")
    print_list(l2)
    print("")
    print("-----------")
    print("")
    res = merge_sorted_lists(l1, l2)
    print_list(res)
    print("")
    print("Is sorted: " + str(check_if_list_sorted(res)))
    print("Is union: " + str(check_if_list_is_union(l1, l2, res)))

if __name__ == "__main__":
    main()