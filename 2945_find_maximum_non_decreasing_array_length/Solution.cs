// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

using System.Collections.Generic;

public class Solution {
    public int FindMaximumLength(int[] nums) {
        int n = nums.Length;
        long[] pref = new long[n + 1], last = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int[] dp = new int[n + 1];
        var dq = new List<(int first, long second)> { (0, 0) };
        for (int i = 1; i <= n; i++) {
            while (dq.Count > 1 && dq[1].second <= pref[i]) dq.RemoveAt(0);
            int j = dq[0].first;
            dp[i] = dp[j] + 1;
            last[i] = pref[i] - pref[j];
            long val = pref[i] + last[i];
            while (dq.Count > 0 && dq[dq.Count - 1].second >= val) dq.RemoveAt(dq.Count - 1);
            dq.Add((i, val));
        }
        return dp[n];
    }
}
