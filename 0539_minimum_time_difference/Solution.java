// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

public class Solution {
    public int findMinDifference(String[] timePoints) {
        int[] minutes = new int[timePoints.length];
        for (int i = 0; i < timePoints.length; i++) {
            String[] parts = timePoints[i].split(":");
            int hour = Integer.parseInt(parts[0]);
            int minute = Integer.parseInt(parts[1]);
            minutes[i] = hour * 60 + minute;
        }

        java.util.Arrays.sort(minutes);
        int best = minutes[minutes.length - 1] - minutes[0];
        for (int i = 1; i < minutes.length; i++) {
            best = Math.min(best, minutes[i] - minutes[i - 1]);
        }
        return Math.min(best, 24 * 60 - minutes[minutes.length - 1] + minutes[0]);
    }
}
