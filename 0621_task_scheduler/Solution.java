// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] counts = new int[26];
        for (char task : tasks) {
            ++counts[task - 'A'];
        }
        int maxFreq = 0;
        for (int count : counts) {
            maxFreq = Math.max(maxFreq, count);
        }
        int maxCount = 0;
        for (int count : counts) {
            if (count == maxFreq) {
                ++maxCount;
            }
        }
        return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount);
    }
}
