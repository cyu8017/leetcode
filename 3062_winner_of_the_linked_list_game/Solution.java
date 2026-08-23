// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public String gameResult(ListNode head) {
        int odd = 0, even = 0;
        for (; head != null; head = head.next.next) {
            int a = head.val, b = head.next.val;
            if (a < b) odd++;
            if (a > b) even++;
        }
        if (odd > even) return "Odd";
        if (odd < even) return "Even";
        return "Tie";
    }
}
