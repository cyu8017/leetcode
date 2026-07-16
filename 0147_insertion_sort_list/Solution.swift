class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func insertionSortList(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        var current = head

        while let node = current {
            var previous = dummy
            while let next = previous.next, next.val < node.val {
                previous = next
            }
            current = node.next
            node.next = previous.next
            previous.next = node
        }
        return dummy.next
    }
}