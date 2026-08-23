// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution {
    private int calc(int[] a1, int[] t1, int[] a2, int[] t2) {
        int minEnd = Integer.MAX_VALUE;
        for (int i = 0; i < a1.length; i++) minEnd = Math.min(minEnd, a1[i] + t1[i]);
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < a2.length; i++) ans = Math.min(ans, Math.max(minEnd, a2[i]) + t2[i]);
        return ans;
    }

    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        return Math.min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration));
    }
}
