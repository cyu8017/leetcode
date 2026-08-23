// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

using System.Collections.Generic;

public class Solution {
    public long[] Distance(int[] nums) {
        int n = nums.Length;
        long[] ans = new long[n];
        var pos = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; ++i) {
            if (!pos.ContainsKey(nums[i])) pos[nums[i]] = new List<int>();
            pos[nums[i]].Add(i);
        }
        foreach (var idxs in pos.Values) {
            int m = idxs.Count;
            long[] pref = new long[m + 1];
            for (int i = 0; i < m; ++i) pref[i + 1] = pref[i] + idxs[i];
            for (int j = 0; j < m; ++j) {
                int idx = idxs[j];
                long left = (long)j * idx - pref[j];
                long right = pref[m] - pref[j + 1] - (long)(m - 1 - j) * idx;
                ans[idx] = left + right;
            }
        }
        return ans;
    }
}
