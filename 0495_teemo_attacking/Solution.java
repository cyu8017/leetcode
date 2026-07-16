// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries.length == 0) {
            return 0;
        }
        int total = duration;
        for (int index = 1; index < timeSeries.length; index++) {
            total += Math.min(duration, timeSeries[index] - timeSeries[index - 1]);
        }
        return total;
    }
}
