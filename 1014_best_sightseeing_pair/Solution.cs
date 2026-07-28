// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

public class Solution {
    public int MaxScoreSightseeingPair(int[] values) {
        int best = values[0], ans = 0;
        for (int j = 1; j < values.Length; j++) {
            ans = Math.Max(ans, best + values[j] - j);
            best = Math.Max(best, values[j] + j);
        }
        return ans;
    }
}
