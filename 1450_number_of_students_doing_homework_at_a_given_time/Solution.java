// LeetCode 1450 - Number Of Students Doing Homework At A Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int ans = 0;
        for (int i = 0; i < startTime.length; i++)
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) ans++;
        return ans;
    }
}
