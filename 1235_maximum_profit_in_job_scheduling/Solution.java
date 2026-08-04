// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import java.util.*;

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++) jobs[i] = new int[]{endTime[i], startTime[i], profit[i]};
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));
        int[] ends = new int[n + 1];
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int end = jobs[i][0], start = jobs[i][1], gain = jobs[i][2];
            int idx = upperBound(ends, start, i);
            ends[i + 1] = end;
            dp[i + 1] = Math.max(dp[i], dp[idx] + gain);
        }
        return dp[n];
    }

    private int upperBound(int[] ends, int target, int limit) {
        int lo = 0, hi = limit;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ends[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

