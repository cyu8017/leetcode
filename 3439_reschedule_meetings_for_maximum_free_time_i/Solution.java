// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.length;
        int[] gaps = new int[n + 1];
        gaps[0] = startTime[0];
        for (int i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
        gaps[n] = eventTime - endTime[n - 1];
        int window = k + 1;
        int sum = 0;
        for (int i = 0; i < window && i < gaps.length; i++) sum += gaps[i];
        int ans = sum;
        for (int i = window; i < gaps.length; i++) {
            sum += gaps[i] - gaps[i - window];
            if (sum > ans) ans = sum;
        }
        return ans;
    }
}
