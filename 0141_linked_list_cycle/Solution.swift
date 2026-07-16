class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        var slow = head
        var fast = head

        while let currentFast = fast, let nextFast = currentFast.next {
            slow = slow?.next
            fast = nextFast.next
            if slow === fast {
                return true
            }
        }
        return false
    }
}