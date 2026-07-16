// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        let dummy = ListNode()
        var current: ListNode? = dummy
        var node1 = l1
        var node2 = l2
        var carry = 0

        while node1 != nil || node2 != nil || carry != 0 {
            var total = carry
            if let n1 = node1 {
                total += n1.val
                node1 = n1.next
            }
            if let n2 = node2 {
                total += n2.val
                node2 = n2.next
            }
            carry = total / 10
            current?.next = ListNode(total % 10)
            current = current?.next
        }

        return dummy.next
    }
}
