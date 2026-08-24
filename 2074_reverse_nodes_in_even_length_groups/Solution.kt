// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun reverseEvenLengthGroups(head: ListNode?): ListNode? {
var dummy: ListNode = ListNode(0, head)
var prev: ListNode = dummy
var group: Int = 1
while (prev.next != null) {
var cur: ListNode = prev.next
var cnt: Int = 0
var node: ListNode = cur
while (node != null && cnt < group) {
node = node.next
cnt++
}
if (cnt % 2 == 0) {
var revPrev: ListNode = node
var p: ListNode = cur
for (i in 0 until cnt) {
var nxt: ListNode = p.next
p.next = revPrev
revPrev = p
p = nxt
}
prev.next = revPrev
prev = cur
}
else {
for (i in 0 until cnt) {
prev = prev.next
}
}
group++
}
return dummy.next
}
}
