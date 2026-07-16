// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

public class Solution {
    public int MinCostII(int[][] costs) {
        if (costs.Length == 0) {
            return 0;
        }
        int colorCount = costs[0].Length;
        int[] previous = (int[])costs[0].Clone();
        for (int row = 1; row < costs.Length; row++) {
            int minCost = previous[0];
            int minIndex = 0;
            for (int color = 1; color < colorCount; color++) {
                if (previous[color] < minCost) {
                    minCost = previous[color];
                    minIndex = color;
                }
            }
            int secondMin = int.MaxValue;
            for (int color = 0; color < colorCount; color++) {
                if (color != minIndex && previous[color] < secondMin) {
                    secondMin = previous[color];
                }
            }
            int[] current = new int[colorCount];
            for (int color = 0; color < colorCount; color++) {
                int extra = color == minIndex ? secondMin : minCost;
                current[color] = costs[row][color] + extra;
            }
            previous = current;
        }
        int result = previous[0];
        for (int color = 1; color < colorCount; color++) {
            if (previous[color] < result) {
                result = previous[color];
            }
        }
        return result;
    }
}
