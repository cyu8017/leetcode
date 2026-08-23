// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

using System.Collections.Generic;

public class Solution {
    public long TaskSchedulerII(int[] tasks, int space) {
        var next = new Dictionary<int, long>();
        long day = 0;
        foreach (int t in tasks) {
            if (next.TryGetValue(t, out long nd) && nd > day) day = nd;
            day++;
            next[t] = day + space;
        }
        return day;
    }
}
