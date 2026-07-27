// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun mergeInBetween(list1: ListNode?, a: Int, b: Int, list2: ListNode?): ListNode? {
        var pre = list1
        repeat(a - 1) { pre = pre!!.next }
        var post = pre
        repeat(b - a + 2) { post = post!!.next }
        pre!!.next = list2
        while (pre!!.next != null) pre = pre.next
        pre!!.next = post
        return list1
    }
}
