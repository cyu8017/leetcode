// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func frequenciesOfElements(_ head: ListNode?) -> ListNode? {
        var cnt: [Int: Int] = [:]
        var node = head
        while let cur = node {
            cnt[cur.val, default: 0] += 1
            node = cur.next
        }
        let dummy = ListNode()
        for val in cnt.values {
            dummy.next = ListNode(val, dummy.next)
        }
        return dummy.next
    }
}
