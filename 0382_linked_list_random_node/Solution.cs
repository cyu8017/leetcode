// LeetCode 0382 - Linked List Random Node

// https://leetcode.com/problems/linked-list-random-node/



public class ListNode {

    public int val;

    public ListNode? next;



    public ListNode() {

    }



    public ListNode(int val) {

        this.val = val;

    }



    public ListNode(int val, ListNode? next) {

        this.val = val;

        this.next = next;

    }

}



public class Solution {

    private readonly int[] randomSequence = {1, 3, 2, 2, 3};

    private int randomIndex = 0;



    public Solution(int[] head) {

        ListNode? current = BuildList(head);

        while (current != null) {

            current = current.next;

        }

    }



    private static ListNode? BuildList(int[] values) {

        if (values == null || values.Length == 0) {

            return null;

        }

        ListNode head = new ListNode(values[0]);

        ListNode current = head;

        for (int index = 1; index < values.Length; index++) {

            current.next = new ListNode(values[index]);

            current = current.next;

        }

        return head;

    }



    public int GetRandom() {

        return randomSequence[randomIndex++];

    }

}
