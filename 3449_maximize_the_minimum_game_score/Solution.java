// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

class Solution {
    public long maxScore(int[] points, int m) {
        long lo = 0, hi = (long) 1e18;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (ok(points, m, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean ok(int[] points, int m, long mid) {
        long need = 0;
        long extra = 0;
        for (int p : points) {
            long req = (mid + p - 1) / p;
            if (req > extra) {
                long visits = req - extra;
                need += 2 * visits - 1;
                extra = visits - 1;
            } else {
                need += 1;
                extra = 0;
            }
            if (need > m) return false;
        }
        return need <= m;
    }
}
