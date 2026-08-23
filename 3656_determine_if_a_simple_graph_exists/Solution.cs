// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

using System;

public class Solution {
    public bool SimpleGraphExists(int[] degrees) {
        int n = degrees.Length;
        int[] d = (int[])degrees.Clone();
        Array.Sort(d, (a, b) => b.CompareTo(a));
        long sum = 0;
        foreach (int x in d) {
            if (x < 0 || x >= n) return false;
            sum += x;
        }
        if (sum % 2 == 1) return false;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + d[i];
        for (int k = 1; k <= n; k++) {
            long right = 0;
            for (int i = k; i < n; i++) right += d[i] < k ? d[i] : k;
            if (prefix[k] > 1L * k * (k - 1) + right) return false;
        }
        return true;
    }
}
