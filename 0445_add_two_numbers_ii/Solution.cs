// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        Stack<int> stack1 = new Stack<int>();
        Stack<int> stack2 = new Stack<int>();
        while (l1 != null) {
            stack1.Push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            stack2.Push(l2.val);
            l2 = l2.next;
        }

        int carry = 0;
        ListNode head = null;
        while (stack1.Count > 0 || stack2.Count > 0 || carry != 0) {
            int total = carry;
            if (stack1.Count > 0) {
                total += stack1.Pop();
            }
            if (stack2.Count > 0) {
                total += stack2.Pop();
            }
            carry = total / 10;
            head = new ListNode(total % 10, head);
        }
        return head;
    }
}
