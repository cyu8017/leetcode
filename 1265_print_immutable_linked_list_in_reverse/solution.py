class ImmutableListNode:
    def printValue(self) -> None: ...
    def getNext(self) -> "ImmutableListNode": ...

class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        if head is None:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()
