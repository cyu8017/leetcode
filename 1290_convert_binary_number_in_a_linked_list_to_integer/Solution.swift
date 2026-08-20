class ListNode {
    var val: Int
    var next: ListNode?
    init() { self.val = 0; self.next = nil }
    init(_ val: Int) { self.val = val; self.next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution {
    func getDecimalValue(_ head: ListNode?) -> Int {
        var ans = 0, node = head
        while let cur = node {
            ans = ans * 2 + cur.val
            node = cur.next
        }
        return ans
    }
}
