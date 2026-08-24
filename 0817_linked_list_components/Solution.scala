// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def numComponents(head: ListNode, nums: Array[Int]): Int = {
    val present = nums.toSet
    var count = 0
    var connected = false
    var cur = head
    while (cur != null) {
      if (present.contains(cur.x)) {
        if (!connected) {
          count += 1
          connected = true
        }
      } else connected = false
      cur = cur.next
    }
    count
  }
}
