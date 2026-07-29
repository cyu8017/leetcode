// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func nextLargerNodes(_ head: ListNode?) -> [Int] {
        var vals = [Int]()
        var cur = head
        while let node = cur {
            vals.append(node.val)
            cur = node.next
        }
        var ans = Array(repeating: 0, count: vals.count)
        var stack = [Int]()
        for (i, x) in vals.enumerated() {
            while let last = stack.last, vals[last] < x {
                ans[stack.removeLast()] = x
            }
            stack.append(i)
        }
        return ans
    }
}
