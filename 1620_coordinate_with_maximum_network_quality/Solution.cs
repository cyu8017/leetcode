// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

using System;

public class Solution {
    public int[] BestCoordinate(int[][] towers, int radius) {
        int[] best = { 0, 0 };
        int quality = -1;
        for (int x = 0; x <= 50; x++) {
            for (int y = 0; y <= 50; y++) {
                int q = 0;
                foreach (var t in towers) {
                    double dx = x - t[0], dy = y - t[1];
                    double d = Math.Sqrt(dx * dx + dy * dy);
                    if (d <= radius) q += (int)(t[2] / (1 + d));
                }
                if (q > quality) {
                    quality = q;
                    best = new[] { x, y };
                }
            }
        }
        return best;
    }
}
