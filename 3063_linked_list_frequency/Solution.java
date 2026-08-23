// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

import java.util.HashMap;
import java.util.Map;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode frequenciesOfElements(ListNode head) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (; head != null; head = head.next)
            cnt.put(head.val, cnt.getOrDefault(head.val, 0) + 1);
        ListNode dummy = new ListNode();
        for (int val : cnt.values())
            dummy.next = new ListNode(val, dummy.next);
        return dummy.next;
    }
}
