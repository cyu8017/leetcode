// LeetCode 0369 - Plus One Linked List

// https://leetcode.com/problems/plus-one-linked-list/



class ListNode(var `val`: Int) {

    var next: ListNode? = null

}



class Solution {

    fun plusOne(head: ListNode?): ListNode? {

        val sentinel = ListNode(0).also { it.next = head }

        var notNine = sentinel

        var node = head



        while (node != null) {

            if (node.`val` != 9) {

                notNine = node

            }

            node = node.next

        }



        notNine.`val`++

        node = notNine.next

        while (node != null) {

            node.`val` = 0

            node = node.next

        }



        return if (sentinel.`val` == 1) sentinel else sentinel.next

    }

}
