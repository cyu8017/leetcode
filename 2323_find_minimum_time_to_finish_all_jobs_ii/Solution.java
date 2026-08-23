// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

import java.util.Arrays;

class Solution {
    public int minimumTime(int[] jobs, int[] workers) {
        Arrays.sort(jobs);
        Arrays.sort(workers);
        int ans = 0;
        for (int i = 0; i < jobs.length; ++i)
            ans = Math.max(ans, (jobs[i] + workers[i] - 1) / workers[i]);
        return ans;
    }
}
