// LeetCode 0369 - Plus One Linked List

// https://leetcode.com/problems/plus-one-linked-list/



class ListNode {

    int val;

    ListNode next;



    ListNode() {}



    ListNode(int val) {

        this.val = val;

    }



    ListNode(int val, ListNode next) {

        this.val = val;

        this.next = next;

    }

}



class Solution {

    public ListNode plusOne(ListNode head) {

        ListNode sentinel = new ListNode(0, head);

        ListNode notNine = sentinel;

        ListNode node = head;



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
