// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def nodesBetweenCriticalPoints(head: ListNode): Array[Int] = {
    val crit = scala.collection.mutable.ArrayBuffer.empty[Int]
    var prev = head
    var cur = head.next
    var idx = 1
    while (cur != null && cur.next != null) {
      if ((cur.x > prev.x && cur.x > cur.next.x) || (cur.x < prev.x && cur.x < cur.next.x))
        crit += idx
      prev = cur
      cur = cur.next
      idx += 1
    }
    if (crit.length < 2) return Array(-1, -1)
    var mn = crit(1) - crit(0)
    var i = 2
    while (i < crit.length) {
      mn = math.min(mn, crit(i) - crit(i - 1))
      i += 1
    }
    Array(mn, crit.last - crit(0))
  }
}
