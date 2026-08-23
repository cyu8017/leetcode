// LeetCode 0369 - Plus One Linked List

// https://leetcode.com/problems/plus-one-linked-list/



public class ListNode {

    public int val;

    public ListNode? next;



    public ListNode(int val = 0, ListNode? next = null) {

        this.val = val;

        this.next = next;

    }

}



public class Solution {

    public ListNode? PlusOne(ListNode? head) {

        ListNode sentinel = new(0, head);

        ListNode notNine = sentinel;

        ListNode? node = head;



        while (node != null) {

            if (node.val != 9) {

                notNine = node;

            }

            node = node.next;

        }



        notNine.val++;

        node = notNine.next;

        while (node != null) {

            node.val = 0;

            node = node.next;

        }



        return sentinel.val == 1 ? sentinel : sentinel.next;

    }

}
