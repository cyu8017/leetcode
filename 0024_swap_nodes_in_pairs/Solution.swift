// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func swapPairs(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0, head)
        var previous: ListNode? = dummy

        while let first = previous?.next, let second = first.next {
            first.next = second.next
            second.next = first
            previous?.next = second
            previous = first
        }

        return dummy.next
    }
}
