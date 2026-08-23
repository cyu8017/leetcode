// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

public class Solution {
    private int best;

    public int MinimumTimeRequired(int[] jobs, int k) {
        Array.Sort(jobs);
        Array.Reverse(jobs);
        int[] loads = new int[k];
        best = jobs.Sum();
        Backtrack(0, jobs, loads);
        return best;
    }

    private void Backtrack(int i, int[] jobs, int[] loads) {
        if (i == jobs.Length) {
            best = Math.Min(best, loads.Max());
            return;
        }
        var seen = new HashSet<int>();
        for (int worker = 0; worker < loads.Length; worker++) {
            if (seen.Contains(loads[worker])) {
                continue;
            }
            if (loads[worker] + jobs[i] >= best) {
                continue;
            }
            seen.Add(loads[worker]);
            loads[worker] += jobs[i];
            Backtrack(i + 1, jobs, loads);
            loads[worker] -= jobs[i];
            if (loads[worker] == 0) {
                break;
            }
        }
    }
}
