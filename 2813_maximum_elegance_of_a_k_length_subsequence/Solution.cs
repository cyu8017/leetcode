// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

using System;
using System.Collections.Generic;

public class Solution {
    public long FindMaximumElegance(int[][] items, int k) {
        Array.Sort(items, (a, b) => b[0].CompareTo(a[0]));
        var seen = new HashSet<int>();
        long total = 0;
        var dup = new List<int>();
        for (int i = 0; i < k; i++) {
            total += items[i][0];
            int c = items[i][1];
            if (seen.Contains(c)) dup.Add(items[i][0]);
            else seen.Add(c);
        }
        long ans = total + 1L * seen.Count * seen.Count;
        for (int i = k; i < items.Length; i++) {
            int c = items[i][1];
            if (seen.Contains(c) || dup.Count == 0) continue;
            total += items[i][0] - dup[^1];
            dup.RemoveAt(dup.Count - 1);
            seen.Add(c);
            ans = Math.Max(ans, total + 1L * seen.Count * seen.Count);
        }
        return ans;
    }
}
