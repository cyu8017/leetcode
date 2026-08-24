// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func numComponents(_ head: ListNode?, _ nums: [Int]) -> Int {
        let present = Set(nums)
        var count = 0
        var connected = false
        var node = head
        while let cur = node {
            if present.contains(cur.val) {
                if !connected {
                    count += 1
                    connected = true
                }
            } else {
                connected = false
            }
            node = cur.next
        }
        return count
    }
}
