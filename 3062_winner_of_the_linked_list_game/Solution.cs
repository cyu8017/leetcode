// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public string GameResult(ListNode head) {
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
