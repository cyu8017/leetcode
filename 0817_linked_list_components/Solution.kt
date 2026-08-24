// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun numComponents(head: ListNode?, nums: IntArray): Int {
        var head = head
        var present = HashSet<Int>()
        for (x in nums) { present.add(x) }
        var count = 0
        var connected = false
        while (head != null) {
            if (present.contains(head.`val`)) {
                if (!connected) {
                    count++
                    connected = true
                }
            } else {
                connected = false
            }
            head = head.next
        }
        return count
    }
}
