// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution {
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long lo = 0, hi = (long) 1e18;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (ok(mid, mountainHeight, workerTimes)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(long t, int mountainHeight, int[] workerTimes) {
        long total = 0;
        for (int w : workerTimes) {
            long l = 0, h = mountainHeight;
            while (l < h) {
                long mid = (l + h + 1) / 2;
                if ((long) w * mid * (mid + 1) / 2 <= t) l = mid;
                else h = mid - 1;
            }
            total += l;
            if (total >= mountainHeight) return true;
        }
        return total >= mountainHeight;
    }
}
