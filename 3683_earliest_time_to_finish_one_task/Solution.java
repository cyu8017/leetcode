// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution {
    public int earliestTime(int[][] tasks) {
        int ans = 200;
        for (var task : tasks) ans = Math.min(ans, task[0] + task[1]);
        return ans;
    }
}
