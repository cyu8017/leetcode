// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { self.val = 0; self.next = nil }
    init(_ val: Int) { self.val = val; self.next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func deleteNodes(_ head: ListNode?, _ m: Int, _ n: Int) -> ListNode? {
        var cur = head
        while cur != nil {
            for _ in 0..<(m - 1) {
                if cur == nil { break }
                cur = cur?.next
            }
            guard let c = cur else { break }
            var drop = c.next
            for _ in 0..<n {
                if drop == nil { break }
                drop = drop?.next
            }
            c.next = drop
            cur = drop
        }
        return head
    }
}
