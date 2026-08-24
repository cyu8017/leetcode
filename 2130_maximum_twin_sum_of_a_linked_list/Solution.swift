// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func pairSum(_ head: ListNode?) -> Int {
        var slow = head, fast = head
        while fast != nil && fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }
        var prev: ListNode?
        while let node = slow {
            let nxt = node.next
            node.next = prev
            prev = node
            slow = nxt
        }
        var ans = 0
        var a = head, b = prev
        while let nodeB = b, let nodeA = a {
            ans = max(ans, nodeA.val + nodeB.val)
            a = nodeA.next
            b = nodeB.next
        }
        return ans
    }
}
