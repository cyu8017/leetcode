// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun sortLinkedList(head: ListNode?): ListNode? {
if (head == null) {
return null
}
var prev: ListNode = head
var cur: ListNode = head.next
while (cur != null) {
if (cur.`val` < 0) {
prev.next = cur.next
cur.next = head
head = cur
cur = prev.next
}
else {
prev = cur
cur = cur.next
}
}
return head
}
}
