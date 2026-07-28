// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

using System.Collections.Generic;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public int[] NextLargerNodes(ListNode head) {
        var vals = new List<int>();
        while (head != null) {
            vals.Add(head.val);
            head = head.next;
        }
        var ans = new int[vals.Count];
        var stack = new Stack<int>();
        for (int i = 0; i < vals.Count; i++) {
            while (stack.Count > 0 && vals[stack.Peek()] < vals[i])
                ans[stack.Pop()] = vals[i];
            stack.Push(i);
        }
        return ans;
    }
}
