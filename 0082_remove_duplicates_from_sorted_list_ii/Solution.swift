// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0, head)
        var previous: ListNode? = dummy
        var current = head

        while current != nil {
            if current?.next != nil && current!.val == current!.next!.val {
                while current?.next != nil && current!.val == current!.next!.val {
                    current = current!.next
                }
                previous?.next = current?.next
            } else {
                previous = previous?.next
            }
            current = current?.next
        }

        return dummy.next
    }
}
