// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

import java.util.*;

class Solution {
    public int minCost(int n, int[] cuts) {
        List<Integer> points = new ArrayList<>();
        points.add(0);
        for (int c : cuts) {
            points.add(c);
        }
        points.add(n);
        Collections.sort(points);
        int size = points.size();
        int[][] dp = new int[size][size];
        for (int width = 2; width < size; width++) {
            for (int left = 0; left + width < size; left++) {
                int right = left + width;
                int best = Integer.MAX_VALUE / 4;
                for (int mid = left + 1; mid < right; mid++) {
                    best = Math.min(best, dp[left][mid] + dp[mid][right]);
                }
                if (right > left + 1) {
                    best += points.get(right) - points.get(left);
                } else {
                    best = 0;
                }
                dp[left][right] = best;
            }
        }
        return dp[0][size - 1];
    }
}
