// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int JobScheduling(int[] startTime, int[] endTime, int[] profit) {
        var jobs = new List<(int end, int start, int gain)>();
        for (int i = 0; i < startTime.Length; i++) {
            jobs.Add((endTime[i], startTime[i], profit[i]));
        }
        jobs.Sort((a, b) => a.end.CompareTo(b.end));
        var ends = new List<int> { 0 };
        var dp = new List<int> { 0 };
        foreach (var (end, start, gain) in jobs) {
            int idx = ends.BinarySearch(start);
            if (idx < 0) idx = ~idx - 1;
            ends.Add(end);
            dp.Add(Math.Max(dp[^1], dp[idx] + gain));
        }
        return dp[^1];
    }
}
