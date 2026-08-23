// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

using System;

public class Solution {
    public int[] RecoverOrder(int[] order, int[] friends) {
        int n = order.Length;
        int[] d = new int[n + 1];
        for (int i = 0; i < n; i++) d[order[i]] = i;
        Array.Sort(friends, (a, b) => d[a].CompareTo(d[b]));
        return friends;
    }
}
