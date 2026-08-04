// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

import java.util.*;

class Solution {
    public int minDayskVariants(int[][] points, int k) {
        int ans = Integer.MAX_VALUE;
        for (int x = 1; x <= 100; x++) {
            for (int y = 1; y <= 100; y++) {
                int[] dists = new int[points.length];
                for (int i = 0; i < points.length; i++) {
                    dists[i] = Math.abs(points[i][0] - x) + Math.abs(points[i][1] - y);
                }
                Arrays.sort(dists);
                ans = Math.min(ans, dists[k - 1]);
            }
        }
        return ans;
    }
}
