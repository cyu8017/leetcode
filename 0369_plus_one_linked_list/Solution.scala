// LeetCode 0369 - Plus One Linked List

// https://leetcode.com/problems/plus-one-linked-list/



class ListNode(var x: Int = 0) {

  var next: ListNode = null

}



object Solution {

  def plusOne(head: ListNode): ListNode = {

    val sentinel = new ListNode(0)

    sentinel.next = head

    var notNine = sentinel

    var node = head



    while (node != null) {

      if (node.x != 9) {

        notNine = node

      }

      node = node.next

    }



    notNine.x += 1

    node = notNine.next

    while (node != null) {

      node.x = 0

      node = node.next

    }



    if (sentinel.x == 1) sentinel else sentinel.next

  }

}
