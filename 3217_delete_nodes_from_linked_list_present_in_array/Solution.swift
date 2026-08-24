// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func modifiedList(_ nums: [Int], _ head: ListNode?) -> ListNode? {
        let s = Set(nums)
        let dummy = ListNode(0, head)
        var pre: ListNode? = dummy
        while let nxt = pre?.next {
            if s.contains(nxt.val) { pre?.next = nxt.next }
            else { pre = nxt }
        }
        return dummy.next
    }
}
