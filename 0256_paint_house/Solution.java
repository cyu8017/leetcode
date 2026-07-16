// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

class Solution {
    public int minCost(int[][] costs) {
        if (costs.length == 0) {
            return 0;
        }
        int[] previous = costs[0].clone();
        for (int row = 1; row < costs.length; row++) {
            int color0 = costs[row][0] + Math.min(previous[1], previous[2]);
            int color1 = costs[row][1] + Math.min(previous[0], previous[2]);
            int color2 = costs[row][2] + Math.min(previous[0], previous[1]);
            previous = new int[] { color0, color1, color2 };
        }
        return Math.min(previous[0], Math.min(previous[1], previous[2]));
    }
}
