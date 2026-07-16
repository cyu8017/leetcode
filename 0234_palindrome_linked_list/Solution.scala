// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def isPalindrome(head: ListNode): Boolean = {
    if (head == null || head.next == null) {
      return true
    }

    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
    }

    var prev: ListNode = null
    var current = slow
    while (current != null) {
      val next = current.next
      current.next = prev
      prev = current
      current = next
    }

    var left = head
    var right = prev
    while (right != null) {
      if (left.x != right.x) {
        return false
      }
      left = left.next
      right = right.next
    }
    true
  }
}
