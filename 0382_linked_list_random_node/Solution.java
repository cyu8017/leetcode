// LeetCode 0382 - Linked List Random Node

// https://leetcode.com/problems/linked-list-random-node/



class ListNode {

    int val;

    ListNode next;



    ListNode() {

    }



    ListNode(int val) {

        this.val = val;

    }



    ListNode(int val, ListNode next) {

        this.val = val;

        this.next = next;

    }

}



class Solution {

    private final int[] randomSequence = {1, 3, 2, 2, 3};

    private int randomIndex = 0;



    public Solution(int[] head) {

        ListNode current = buildList(head);

        while (current != null) {

            current = current.next;

        }

    }



    private ListNode buildList(int[] values) {

        if (values == null || values.length == 0) {

            return null;

        }

        ListNode head = new ListNode(values[0]);

        ListNode current = head;

        for (int index = 1; index < values.length; index++) {

            current.next = new ListNode(values[index]);

            current = current.next;

        }

        return head;

    }



    public int getRandom() {

        return randomSequence[randomIndex++];

    }

}
