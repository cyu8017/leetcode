// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

using System.Collections.Generic;

public class Solution {
    public IList<int> LongestCommonSubsequence(int[][] arrays) {
        var cnt = new Dictionary<int, int>();
        foreach (var arr in arrays)
            foreach (int x in arr)
                cnt[x] = cnt.GetValueOrDefault(x) + 1;
        int m = arrays.Length;
        var ans = new List<int>();
        foreach (int x in arrays[0])
            if (cnt[x] == m) ans.Add(x);
        return ans;
    }
}