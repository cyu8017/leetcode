// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func reverseKGroup(_ head: ListNode?, _ k: Int) -> ListNode? {
        let dummy = ListNode(0, head)
        var groupPrevious: ListNode? = dummy

        while true {
            var kth: ListNode? = groupPrevious
            for _ in 0..<k {
                kth = kth?.next
                if kth == nil {
                    return dummy.next
                }
            }

            let groupNext = kth?.next
            var previous: ListNode? = groupNext
            var current = groupPrevious?.next

            while current !== groupNext {
                let next = current?.next
                current?.next = previous
                previous = current
                current = next
            }

            let tmp = groupPrevious?.next
            groupPrevious?.next = kth
            groupPrevious = tmp
        }
    }
}
