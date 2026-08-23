// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

using System;

public class Solution {
    public long MaximumImportance(int n, int[][] roads) {
        int[] deg = new int[n];
        foreach (var r in roads) { deg[r[0]]++; deg[r[1]]++; }
        Array.Sort(deg);
        long ans = 0;
        for (int i = 0; i < n; i++) ans += (long)deg[i] * (i + 1);
        return ans;
    }
}
