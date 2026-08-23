// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        List<Integer> crit = new ArrayList<>();
        ListNode prev = head, cur = head.next;
        int idx = 1;
        while (cur != null && cur.next != null) {
            if ((cur.val > prev.val && cur.val > cur.next.val) ||
                (cur.val < prev.val && cur.val < cur.next.val))
                crit.add(idx);
            prev = cur; cur = cur.next; idx++;
        }
        if (crit.size() < 2) return new int[] { -1, -1 };
        int mn = crit.get(1) - crit.get(0);
        for (int i = 2; i < crit.size(); i++) mn = Math.min(mn, crit.get(i) - crit.get(i - 1));
        return new int[] { mn, crit.get(crit.size() - 1) - crit.get(0) };
    }
}
