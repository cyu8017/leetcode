// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

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
        var dummy = new ListNode();
        var current = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int total = carry;
            if (l1 != null) {
                total += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                total += l2.val;
                l2 = l2.next;
            }
            carry = total / 10;
            current.next = new ListNode(total % 10);
            current = current.next;
        }

        return dummy.next;
    }
}
