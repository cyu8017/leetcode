// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

import java.util.*;

class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        int[] xs = new int[points.length];
        for (int i = 0; i < points.length; i++) xs[i] = points[i][0];
        Arrays.sort(xs);
        int ans = 0;
        for (int i = 1; i < xs.length; i++) ans = Math.max(ans, xs[i] - xs[i - 1]);
        return ans;
    }
}
