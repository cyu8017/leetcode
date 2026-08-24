// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null

    constructor(`val`: Int, next: ListNode?) : this(`val`) {
        this.next = next
    }
}

class Solution {
    fun modifiedList(nums: IntArray, head: ListNode?): ListNode? {
        val s = HashSet<Int>()
        for (x in nums) s.add(x)
        val dummy = ListNode(0, head)
        var pre: ListNode? = dummy
        while (pre!!.next != null) {
            if (s.contains(pre.next!!.`val`)) {
                pre.next = pre.next!!.next
            } else {
                pre = pre.next
            }
        }
        return dummy.next
    }
}
