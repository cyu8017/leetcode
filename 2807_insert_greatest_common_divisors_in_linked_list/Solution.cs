// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode InsertGreatestCommonDivisors(ListNode head) {
        int Gcd(int a, int b) {
            while (b != 0) { int t = a % b; a = b; b = t; }
            return a;
        }
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            int g = Gcd(cur.val, cur.next.val);
            ListNode node = new ListNode(g, cur.next);
            cur.next = node;
            cur = node.next;
        }
        return head;
    }
}
