// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

import scala.collection.mutable

class ListNode(_x: Int = 0) {
  var x: Int = _x
  var next: ListNode = null
}

object Solution {
  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    val stack1 = mutable.Stack.empty[Int]
    val stack2 = mutable.Stack.empty[Int]
    var node1 = l1
    var node2 = l2
    while (node1 != null) {
      stack1.push(node1.x)
      node1 = node1.next
    }
    while (node2 != null) {
      stack2.push(node2.x)
      node2 = node2.next
    }

    var carry = 0
    var head: ListNode = null
    while (stack1.nonEmpty || stack2.nonEmpty || carry != 0) {
      var total = carry
      if (stack1.nonEmpty) {
        total += stack1.pop()
      }
      if (stack2.nonEmpty) {
        total += stack2.pop()
      }
      carry = total / 10
      val node = new ListNode(total % 10)
      node.next = head
      head = node
    }
    head
  }
}
