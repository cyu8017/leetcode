// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil }
    public init(_ val: Int) { self.val = val; self.next = nil }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func insertGreatestCommonDivisors(_ head: ListNode?) -> ListNode? {
        var cur = head
        while let node = cur, let nxt = node.next {
            let g = gcd(node.val, nxt.val)
            node.next = ListNode(g, nxt)
            cur = node.next?.next
        }
        return head
    }

    private func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
