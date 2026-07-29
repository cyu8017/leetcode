// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def nextLargerNodes(head: ListNode): Array[Int] = {
    val vals = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      vals += cur.x
      cur = cur.next
    }
    val ans = Array.fill(vals.length)(0)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- vals.indices) {
      while (stack.nonEmpty && vals(stack.last) < vals(i)) {
        ans(stack.remove(stack.length - 1)) = vals(i)
      }
      stack += i
    }
    ans
  }
}
