// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func deleteDuplicatesUnsorted(_ head: ListNode?) -> ListNode? {
        var counts = [Int: Int]()
        var node = head
        while let cur = node {
            counts[cur.val, default: 0] += 1
            node = cur.next
        }
        let dummy = ListNode(0, head)
        var prev: ListNode? = dummy
        node = head
        while let cur = node {
            if counts[cur.val, default: 0] > 1 {
                prev?.next = cur.next
                node = cur.next
            } else {
                prev = cur
                node = cur.next
            }
        }
        return dummy.next
    }
}
