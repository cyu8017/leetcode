// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

import java.util.*;

class Solution {
    public int visiblePoints(int[][] points, int angle, int[] location) {
        int same = 0;
        List<Double> a = new ArrayList<>();
        int lx = location[0], ly = location[1];
        for (int[] p : points) {
            int dx = p[0] - lx, dy = p[1] - ly;
            if (dx == 0 && dy == 0) same++;
            else a.add(Math.atan2(dy, dx));
        }
        Collections.sort(a);
        int n = a.size();
        for (int i = 0; i < n; i++) a.add(a.get(i) + 2 * Math.PI);
        double width = Math.toRadians(angle) + 1e-12;
        int left = 0, best = 0;
        for (int right = 0; right < a.size(); right++) {
            while (a.get(right) - a.get(left) > width) left++;
            best = Math.max(best, Math.min(n, right - left + 1));
        }
        return best + same;
    }
}
