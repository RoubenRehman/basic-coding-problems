from copy import copy
from ListHelpers.ListHelpers import ListNode, print_list, create_random_ordered_list, copy_list

def reverse_list(head: ListNode) -> ListNode:
    head = copy_list(head)

    if head is None:
        return None

    if head.next is None:
        return head

    temp = head.next
    head.next = None

    while(temp.next):
        hold = temp.next
        temp.next = head
        head = temp
        temp = hold

    temp.next = head
    return temp

def main():

    head = create_random_ordered_list()

    print_list(head)
    print("-------")
    head = reverse_list(head)
    print_list(head)




if __name__ == "__main__":
    main()


