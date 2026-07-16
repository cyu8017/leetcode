// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

import java.util.PriorityQueue

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        val heap = PriorityQueue<Triple<Int, Int, ListNode>>(compareBy({ it.first }, { it.second }))
        var order = 0

        for (node in lists) {
            if (node != null) {
                heap.offer(Triple(node.`val`, order++, node))
            }
        }

        val dummy = ListNode(0)
        var current: ListNode? = dummy

        while (heap.isNotEmpty()) {
            val node = heap.poll().third
            current!!.next = node
            current = current.next
            val next = node.next
            if (next != null) {
                heap.offer(Triple(next.`val`, order++, next))
            }
        }

        return dummy.next
    }
}
