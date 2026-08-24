// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil }
    public init(_ val: Int) { self.val = val; self.next = nil }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func doubleIt(_ head: ListNode?) -> ListNode? {
        var head = rev(head)
        var carry = 0
        var cur = head
        var prev: ListNode? = nil
        while let node = cur {
            let val = node.val * 2 + carry
            node.val = val % 10
            carry = val / 10
            prev = node
            cur = node.next
        }
        if carry > 0 { prev?.next = ListNode(carry) }
        return rev(head)
    }

    private func rev(_ node0: ListNode?) -> ListNode? {
        var node = node0
        var prev: ListNode? = nil
        while let cur = node {
            let nxt = cur.next
            cur.next = prev
            prev = cur
            node = nxt
        }
        return prev
    }
}
