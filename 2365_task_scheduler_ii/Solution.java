// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long taskSchedulerII(int[] tasks, int space) {
        Map<Integer, Long> next = new HashMap<>();
        long day = 0;
        for (int t : tasks) {
            day = Math.max(day, next.getOrDefault(t, 0L));
            day++;
            next.put(t, day + space);
        }
        return day;
    }
}
