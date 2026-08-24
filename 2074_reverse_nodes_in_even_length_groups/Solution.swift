// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func reverseEvenLengthGroups(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0, head)
        var prev: ListNode? = dummy
        var group = 1
        while prev?.next != nil {
            var cur = prev?.next
            var cnt = 0
            var node = cur
            while node != nil && cnt < group {
                node = node?.next
                cnt += 1
            }
            if cnt % 2 == 0 {
                var revPrev = node
                var p = cur
                for _ in 0..<cnt {
                    let nxt = p?.next
                    p?.next = revPrev
                    revPrev = p
                    p = nxt
                }
                prev?.next = revPrev
                prev = cur
            } else {
                for _ in 0..<cnt { prev = prev?.next }
            }
            group += 1
        }
        return dummy.next
    }
}
