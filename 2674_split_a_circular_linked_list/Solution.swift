// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil }
    public init(_ val: Int) { self.val = val; self.next = nil }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func splitCircularLinkedList(_ list: ListNode?) -> [ListNode?] {
        guard let list = list else { return [nil, nil] }
        var slow: ListNode? = list
        var fast: ListNode? = list
        while fast?.next !== list && fast?.next?.next !== list {
            slow = slow?.next
            fast = fast?.next?.next
        }
        if fast?.next?.next === list { fast = fast?.next }
        let head2 = slow?.next
        slow?.next = list
        fast?.next = head2
        return [list, head2]
    }
}
