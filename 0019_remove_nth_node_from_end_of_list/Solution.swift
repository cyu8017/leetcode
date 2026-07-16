// LeetCode 0019 - Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        let dummy = ListNode(0, head)
        var fast: ListNode? = dummy
        var slow: ListNode? = dummy

        for _ in 0..<n {
            fast = fast?.next
        }

        while fast?.next != nil {
            fast = fast?.next
            slow = slow?.next
        }

        slow?.next = slow?.next?.next
        return dummy.next
    }
}
