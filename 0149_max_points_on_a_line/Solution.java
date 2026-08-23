// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

import java.util.*;
class Solution {
    public int maxPoints(int[][] points) {
        int best = 0;
        for (int i = 0; i < points.length; i++) {
            Map<String, Integer> slopes = new HashMap<>();
            int local = 1;
            for (int j = i + 1; j < points.length; j++) {
                int dx = points[j][0] - points[i][0], dy = points[j][1] - points[i][1];
                int gcd = gcd(dx, dy); dx /= gcd; dy /= gcd;
                if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy; }
                String key = dx + "," + dy;
                local = Math.max(local, slopes.merge(key, 1, Integer::sum) + 1);
            }
            best = Math.max(best, local);
        }
        return best;
    }
    private int gcd(int a, int b) { a = Math.abs(a); b = Math.abs(b); while (b != 0) { int temp = a % b; a = b; b = temp; } return a; }
}