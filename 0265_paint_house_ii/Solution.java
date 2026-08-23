// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

import java.util.Arrays;

class Solution {
    public int minCostII(int[][] costs) {
        if (costs.length == 0) {
            return 0;
        }
        int colorCount = costs[0].length;
        int[] previous = Arrays.copyOf(costs[0], colorCount);
        for (int row = 1; row < costs.length; row++) {
            int minCost = Arrays.stream(previous).min().getAsInt();
            int minIndex = 0;
            for (int i = 0; i < colorCount; i++) {
                if (previous[i] == minCost) {
                    minIndex = i;
                    break;
                }
            }
            int secondMin = Integer.MAX_VALUE;
            for (int i = 0; i < colorCount; i++) {
                if (i != minIndex) {
                    secondMin = Math.min(secondMin, previous[i]);
                }
            }
            int[] current = new int[colorCount];
            for (int color = 0; color < colorCount; color++) {
                int extra = color == minIndex ? secondMin : minCost;
                current[color] = costs[row][color] + extra;
            }
            previous = current;
        }
        return Arrays.stream(previous).min().getAsInt();
    }
}
