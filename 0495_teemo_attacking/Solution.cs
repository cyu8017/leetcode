// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

public class Solution {
    public int FindPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries.Length == 0) {
            return 0;
        }
        int total = duration;
        for (int index = 1; index < timeSeries.Length; index++) {
            total += Math.Min(duration, timeSeries[index] - timeSeries[index - 1]);
        }
        return total;
    }
}
