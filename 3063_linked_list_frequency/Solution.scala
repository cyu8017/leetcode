// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def frequenciesOfElements(head: ListNode): ListNode = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var cur = head
    while (cur != null) {
      cnt(cur.x) = cnt.getOrElse(cur.x, 0) + 1
      cur = cur.next
    }
    val dummy = new ListNode()
    cnt.values.foreach { v =>
      dummy.next = new ListNode(v, dummy.next)
    }
    dummy.next
  }
}
