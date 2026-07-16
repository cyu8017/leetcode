class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func sortList(_ head: ListNode?) -> ListNode? {
        guard let head, head.next != nil else { return head }

        var slow: ListNode? = head
        var fast: ListNode? = head
        var previous: ListNode?
        while fast != nil && fast?.next != nil {
            previous = slow
            slow = slow?.next
            fast = fast?.next?.next
        }
        previous?.next = nil

        return merge(sortList(head), sortList(slow))
    }

    private func merge(_ left: ListNode?, _ right: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        var tail = dummy
        var left = left
        var right = right

        while let leftNode = left, let rightNode = right {
            if leftNode.val <= rightNode.val {
                tail.next = leftNode
                left = leftNode.next
            } else {
                tail.next = rightNode
                right = rightNode.next
            }
            tail = tail.next!
        }
        tail.next = left ?? right
        return dummy.next
    }
}