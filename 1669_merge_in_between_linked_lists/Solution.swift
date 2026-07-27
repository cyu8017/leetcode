// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func mergeInBetween(_ list1: ListNode?, _ a: Int, _ b: Int, _ list2: ListNode?) -> ListNode? {
        var pre = list1
        for _ in 0..<(a - 1) { pre = pre?.next }
        var post = pre
        for _ in 0..<(b - a + 2) { post = post?.next }
        pre?.next = list2
        while pre?.next != nil { pre = pre?.next }
        pre?.next = post
        return list1
    }
}
