// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

class Solution {
    public int[] bestCoordinate(int[][] towers, int radius) {
        int[] best = new int[] {0, 0};
        int quality = -1;
        for (int x = 0; x <= 50; x++) {
            for (int y = 0; y <= 50; y++) {
                int q = 0;
                for (int[] t : towers) {
                    double d = Math.hypot(x - t[0], y - t[1]);
                    if (d <= radius) q += (int) (t[2] / (1 + d));
                }
                if (q > quality) {
                    quality = q;
                    best = new int[] {x, y};
                }
            }
        }
        return best;
    }
}
