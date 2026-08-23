// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

using System;

public class Solution {
    public int EarliestTime(int[][] tasks) {
        int ans = 200;
        foreach (var task in tasks) ans = Math.Min(ans, task[0] + task[1]);
        return ans;
    }
}
