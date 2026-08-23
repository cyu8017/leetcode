// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

public class Solution {
    public long MaxScore(int[] points, int m) {
        bool Ok(long mid) {
            long need = 0;
            long extra = 0;
            foreach (int p in points) {
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
        long lo = 0, hi = (long)1e18;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
