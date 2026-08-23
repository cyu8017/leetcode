// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

using System;
using System.Linq;

public class Solution {
    public int MinDeletionSize(string[] strs) {
        int m = strs[0].Length;
        int[] dp = Enumerable.Repeat(1, m).ToArray();
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < j; i++) {
                bool ok = true;
                foreach (var row in strs) {
                    if (row[i] > row[j]) { ok = false; break; }
                }
                if (ok) dp[j] = Math.Max(dp[j], dp[i] + 1);
            }
        }
        return m - dp.Max();
    }
}
