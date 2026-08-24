// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def pairSum(head: ListNode): Int = {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
    }
    var prev: ListNode = null
    while (slow != null) {
      val nxt = slow.next
      slow.next = prev
      prev = slow
      slow = nxt
    }
    var ans = 0
    var a = head
    var b = prev
    while (b != null) {
      ans = math.max(ans, a.x + b.x)
      a = a.next
      b = b.next
    }
    ans
  }
}
