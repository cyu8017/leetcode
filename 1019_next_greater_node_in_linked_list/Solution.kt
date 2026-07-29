// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun nextLargerNodes(head: ListNode?): IntArray {
        val vals = mutableListOf<Int>()
        var cur = head
        while (cur != null) {
            vals.add(cur.`val`)
            cur = cur.next
        }
        val ans = IntArray(vals.size)
        val stack = ArrayDeque<Int>()
        for (i in vals.indices) {
            while (stack.isNotEmpty() && vals[stack.last()] < vals[i]) {
                ans[stack.removeLast()] = vals[i]
            }
            stack.addLast(i)
        }
        return ans
    }
}
