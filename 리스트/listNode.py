class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode') -> None:
        self.item = newItem
        self.next = nextNode
