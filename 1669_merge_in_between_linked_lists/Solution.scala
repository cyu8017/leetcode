// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def mergeInBetween(list1: ListNode, a: Int, b: Int, list2: ListNode): ListNode = {
    var pre = list1
    for (_ <- 0 until a - 1) pre = pre.next
    var post = pre
    for (_ <- 0 until b - a + 2) post = post.next
    pre.next = list2
    while (pre.next != null) pre = pre.next
    pre.next = post
    list1
  }
}
