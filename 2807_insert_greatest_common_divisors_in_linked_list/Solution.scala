// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def insertGreatestCommonDivisors(head: ListNode): ListNode = {
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var cur = head
    while (cur != null && cur.next != null) {
      val g = gcd(cur.x, cur.next.x)
      val node = new ListNode(g, cur.next)
      cur.next = node
      cur = node.next
    }
    head
  }
}
