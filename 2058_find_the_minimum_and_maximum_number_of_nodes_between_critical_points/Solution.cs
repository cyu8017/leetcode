// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

using System;
using System.Collections.Generic;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) { this.val = val; this.next = next; }
}

public class Solution {
    public int[] NodesBetweenCriticalPoints(ListNode head) {
        var crit = new List<int>();
        ListNode prev = head, cur = head.next;
        int idx = 1;
        while (cur != null && cur.next != null) {
            if ((cur.val > prev.val && cur.val > cur.next.val) ||
                (cur.val < prev.val && cur.val < cur.next.val))
                crit.Add(idx);
            prev = cur; cur = cur.next; idx++;
        }
        if (crit.Count < 2) return new[] { -1, -1 };
        int mn = crit[1] - crit[0];
        for (int i = 2; i < crit.Count; i++) mn = Math.Min(mn, crit[i] - crit[i - 1]);
        return new[] { mn, crit[crit.Count - 1] - crit[0] };
    }
}
