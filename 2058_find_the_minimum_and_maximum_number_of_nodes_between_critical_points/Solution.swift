// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func nodesBetweenCriticalPoints(_ head: ListNode?) -> [Int] {
        var crit = [Int]()
        var prev = head
        var cur = head?.next
        var idx = 1
        while let node = cur, let nxt = node.next, let p = prev {
            if (node.val > p.val && node.val > nxt.val) || (node.val < p.val && node.val < nxt.val) {
                crit.append(idx)
            }
            prev = node
            cur = nxt
            idx += 1
        }
        if crit.count < 2 { return [-1, -1] }
        var mn = crit[1] - crit[0]
        for i in 2..<crit.count { mn = min(mn, crit[i] - crit[i - 1]) }
        return [mn, crit[crit.count - 1] - crit[0]]
    }
}
