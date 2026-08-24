// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil }
    public init(_ val: Int) { self.val = val; self.next = nil }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func removeNodes(_ head: ListNode?) -> ListNode? {
        func rev(_ node: ListNode?) -> ListNode? {
            var prev: ListNode? = nil
            var node = node
            while node != nil {
                let nxt = node!.next
                node!.next = prev
                prev = node
                node = nxt
            }
            return prev
        }
        var head = rev(head)
        var mx = 0
        let dummy = ListNode(0, head)
        var prev: ListNode? = dummy
        while prev?.next != nil {
            if prev!.next!.val >= mx {
                mx = prev!.next!.val
                prev = prev!.next
            } else {
                prev!.next = prev!.next!.next
            }
        }
        return rev(dummy.next)
    }
}
