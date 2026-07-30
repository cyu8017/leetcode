// LeetCode 1450 - Number Of Students Doing Homework At A Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

public class Solution {
    public int BusyStudent(int[] startTime, int[] endTime, int queryTime) {
        int ans = 0;
        for (int i = 0; i < startTime.Length; i++)
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) ans++;
        return ans;
    }
}
