// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

using System;

public class Solution {
    public long MaxProfit(int[] workers, int[][] tasks) {
        Array.Sort(workers);
        Array.Sort(tasks, (a, b) => a[0].CompareTo(b[0]));
        long ans = 0;
        bool[] used = new bool[tasks.Length];
        foreach (int w in workers) {
            int best = -1, bi = -1;
            for (int i = 0; i < tasks.Length; i++) {
                if (used[i]) continue;
                if (tasks[i][0] > w) break;
                if (tasks[i][1] > best) {
                    best = tasks[i][1];
                    bi = i;
                }
            }
            if (bi >= 0) {
                used[bi] = true;
                ans += best;
            }
        }
        return ans;
    }
}
