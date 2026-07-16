// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

public class Solution {
    public int MinCost(int[][] costs) {
        if (costs.Length == 0) {
            return 0;
        }
        int[] previous = (int[])costs[0].Clone();
        for (int row = 1; row < costs.Length; row++) {
            previous = new int[] {
                costs[row][0] + System.Math.Min(previous[1], previous[2]),
                costs[row][1] + System.Math.Min(previous[0], previous[2]),
                costs[row][2] + System.Math.Min(previous[0], previous[1]),
            };
        }
        return System.Math.Min(previous[0], System.Math.Min(previous[1], previous[2]));
    }
}
