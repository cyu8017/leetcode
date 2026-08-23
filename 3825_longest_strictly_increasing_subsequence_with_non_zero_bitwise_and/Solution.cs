// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

using System;
using System.Collections.Generic;

public class Solution {
    static int BitLen(uint x) {
        if (x == 0) return 0;
        int n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    }

    static int Lis(List<int> arr) {
        var g = new List<int>();
        foreach (int x in arr) {
            int idx = g.BinarySearch(x);
            if (idx < 0) idx = ~idx;
            if (idx == g.Count) g.Add(x);
            else g[idx] = x;
        }
        return g.Count;
    }

    public int LongestSubsequence(int[] nums) {
        int ans = 0;
        int mx = 0;
        foreach (int x in nums) mx = Math.Max(mx, x);
        int m = BitLen((uint)mx);
        for (int i = 0; i < m; i++) {
            var arr = new List<int>();
            foreach (int x in nums) {
                if (((x >> i) & 1) != 0) arr.Add(x);
            }
            ans = Math.Max(ans, Lis(arr));
        }
        return ans;
    }
}
