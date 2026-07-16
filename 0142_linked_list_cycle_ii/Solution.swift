class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func detectCycle(_ head: ListNode?) -> ListNode? {
        var slow = head
        var fast = head

        while let currentFast = fast, let nextFast = currentFast.next {
            slow = slow?.next
            fast = nextFast.next
            if slow === fast {
                slow = head
                while slow !== fast {
                    slow = slow?.next
                    fast = fast?.next
                }
                return slow
            }
        }
        return nil
    }
}