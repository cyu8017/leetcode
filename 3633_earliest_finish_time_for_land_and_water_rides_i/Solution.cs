// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

using System;

public class Solution {
    int Calc(int[] a1, int[] t1, int[] a2, int[] t2) {
        int minEnd = int.MaxValue;
        for (int i = 0; i < a1.Length; i++) minEnd = Math.Min(minEnd, a1[i] + t1[i]);
        int ans = int.MaxValue;
        for (int i = 0; i < a2.Length; i++) ans = Math.Min(ans, Math.Max(minEnd, a2[i]) + t2[i]);
        return ans;
    }

    public int EarliestFinishTime(int[] landStartTime, int[] landDuration,
                                  int[] waterStartTime, int[] waterDuration) {
        return Math.Min(Calc(landStartTime, landDuration, waterStartTime, waterDuration),
                        Calc(waterStartTime, waterDuration, landStartTime, landDuration));
    }
}
