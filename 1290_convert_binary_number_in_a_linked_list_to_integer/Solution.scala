// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def getDecimalValue(head: ListNode): Int = {
    var value = 0
    var cur = head
    while (cur != null) {
      value = value * 2 + cur.x
      cur = cur.next
    }
    value
  }
}
