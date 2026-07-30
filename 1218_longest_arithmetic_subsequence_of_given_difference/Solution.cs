// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LongestSubsequence(int[] arr, int difference) {
        var dp = new Dictionary<int, int>();
        foreach (int x in arr) dp[x] = dp.GetValueOrDefault(x - difference) + 1;
        return dp.Values.Max();
    }
}
