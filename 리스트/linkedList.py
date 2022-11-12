from 리스트.listNode import ListNode


class LinkedList:
    # 초기화
    def __init__(self) -> None:
        self.__head = ListNode
        self.__numItems = 0

    # 내부에서 i 번째
    def __getNode(self, i: int) -> ListNode:
        curr = self.__head

        for _ in range(i + 1):
            curr = curr.next

        return curr

    def __findNode(self, x) -> tuple(ListNode, ListNode):
        prev = self.__head
        curr = prev.next

        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev, curr = curr, curr.next

        return (None, None)

    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print("에러 처리")
