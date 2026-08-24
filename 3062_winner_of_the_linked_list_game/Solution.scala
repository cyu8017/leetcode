// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def gameResult(head: ListNode): String = {
    var odd = 0
    var even = 0
    var cur = head
    while (cur != null) {
      val a = cur.x
      val b = cur.next.x
      if (a < b) odd += 1
      if (a > b) even += 1
      cur = cur.next.next
    }
    if (odd > even) "Odd"
    else if (odd < even) "Even"
    else "Tie"
  }
}
