// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

import java.util.HashMap;
import java.util.Map;

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
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        Map<Integer, Integer> counts = new HashMap<>();
        ListNode node = head;
        while (node != null) {
            counts.merge(node.val, 1, Integer::sum);
            node = node.next;
        }

        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        node = head;
        while (node != null) {
            if (counts.get(node.val) > 1) {
                prev.next = node.next;
                node = node.next;
            } else {
                prev = node;
                node = node.next;
            }
        }
        return dummy.next;
    }
}
