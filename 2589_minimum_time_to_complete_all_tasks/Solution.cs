// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

using System;

public class Solution {
    public int FindMinimumTime(int[][] tasks) {
        Array.Sort(tasks, (a, b) => a[1].CompareTo(b[1]));
        bool[] used = new bool[2001];
        int ans = 0;
        foreach (var t in tasks) {
            int start = t[0], end = t[1], dur = t[2];
            int have = 0;
            for (int i = start; i <= end; ++i) if (used[i]) have++;
            int need = dur - have;
            for (int i = end; i >= start && need > 0; --i) {
                if (!used[i]) {
                    used[i] = true;
                    need--;
                    ans++;
                }
            }
        }
        return ans;
    }
}
