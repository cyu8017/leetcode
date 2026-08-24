// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun frequenciesOfElements(head: ListNode?): ListNode? {
        val cnt = HashMap<Int, Int>()
        var node = head
        while (node != null) {
            cnt[node.`val`] = cnt.getOrDefault(node.`val`, 0) + 1
            node = node.next
        }
        var dummy = ListNode()
        for (v in cnt.values) {
            dummy.next = ListNode(v).also { it.next = dummy.next }
        }
        return dummy.next
    }
}
