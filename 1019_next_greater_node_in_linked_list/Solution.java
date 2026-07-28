// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> vals = new ArrayList<>();
        while (head != null) {
            vals.add(head.val);
            head = head.next;
        }
        int[] ans = new int[vals.size()];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < vals.size(); i++) {
            while (!stack.isEmpty() && vals.get(stack.peek()) < vals.get(i)) {
                ans[stack.pop()] = vals.get(i);
            }
            stack.push(i);
        }
        return ans;
    }
}
