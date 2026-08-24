// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun nodesBetweenCriticalPoints(head: ListNode?): IntArray {
var crit: MutableList<Int> = mutableListOf()
var prev: ListNode = head
var cur: ListNode = head.next
var idx: Int = 1
while (cur != null && cur.next != null) {
if ((cur.`val` > prev.`val` && cur.`val` > cur.next.`val`) ||
                (cur.`val` < prev.`val` && cur.`val` < cur.next.`val`)) {
crit.add(idx)
}
prev = cur
cur = cur.next
idx++
}
if (crit.size < 2) {
return intArrayOf( -1, -1 )
}
var mn: Int = crit[1] - crit[0]
for (i in 2 until crit.size) {
mn = minOf(mn, crit[i] - crit[i - 1])
}
return intArrayOf( mn, crit[crit.size - 1] - crit[0] )
}
}
