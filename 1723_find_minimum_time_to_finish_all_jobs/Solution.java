// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    private int best;

    public int minimumTimeRequired(int[] jobs, int k) {
        Arrays.sort(jobs);
        for (int lo = 0, hi = jobs.length - 1; lo < hi; lo++, hi--) {
            int temp = jobs[lo];
            jobs[lo] = jobs[hi];
            jobs[hi] = temp;
        }
        int[] loads = new int[k];
        best = 0;
        for (int job : jobs) {
            best += job;
        }
        backtrack(0, jobs, loads);
        return best;
    }

    private void backtrack(int i, int[] jobs, int[] loads) {
        if (i == jobs.length) {
            int max = 0;
            for (int load : loads) {
                max = Math.max(max, load);
            }
            best = Math.min(best, max);
            return;
        }
        Set<Integer> seen = new HashSet<>();
        for (int worker = 0; worker < loads.length; worker++) {
            if (seen.contains(loads[worker])) {
                continue;
            }
            if (loads[worker] + jobs[i] >= best) {
                continue;
            }
            seen.add(loads[worker]);
            loads[worker] += jobs[i];
            backtrack(i + 1, jobs, loads);
            loads[worker] -= jobs[i];
            if (loads[worker] == 0) {
                break;
            }
        }
    }
}
