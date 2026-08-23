// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

using System;

public class Solution {
    public int MinimumTime(int[] jobs, int[] workers) {
        Array.Sort(jobs);
        Array.Sort(workers);
        int ans = 0;
        for (int i = 0; i < jobs.Length; ++i)
            ans = Math.Max(ans, (jobs[i] + workers[i] - 1) / workers[i]);
        return ans;
    }
}
