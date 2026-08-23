// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

using System;

public class Solution {
    public int MaxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int m = difficulty.Length;
        var jobs = new (int d, int p)[m];
        for (int i = 0; i < m; i++) jobs[i] = (difficulty[i], profit[i]);
        Array.Sort(jobs, (a, b) => a.d.CompareTo(b.d));
        Array.Sort(worker);
        int ans = 0, best = 0, iJob = 0;
        foreach (int ability in worker) {
            while (iJob < m && jobs[iJob].d <= ability) {
                best = Math.Max(best, jobs[iJob].p);
                iJob++;
            }
            ans += best;
        }
        return ans;
    }
}
