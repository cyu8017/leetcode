// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        int[] counts = new int[26];
        foreach (char task in tasks) ++counts[task - 'A'];
        int maxFreq = 0;
        foreach (int count in counts) if (count > maxFreq) maxFreq = count;
        int maxCount = 0;
        foreach (int count in counts) if (count == maxFreq) ++maxCount;
        return System.Math.Max(tasks.Length, (maxFreq - 1) * (n + 1) + maxCount);
    }
}
