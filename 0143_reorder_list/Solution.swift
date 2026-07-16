class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func reorderList(_ head: ListNode?) {
        guard let head, head.next != nil else { return }
        var slow: ListNode? = head
        var fast: ListNode? = head

        while fast?.next?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }

        var second = slow?.next
        slow?.next = nil
        var previous: ListNode?
        while let node = second {
            second = node.next
            node.next = previous
            previous = node
        }

        var first: ListNode? = head
        second = previous
        while let secondNode = second {
            let firstNext = first?.next
            second = secondNode.next
            first?.next = secondNode
            secondNode.next = firstNext
            first = firstNext
        }
    }
}