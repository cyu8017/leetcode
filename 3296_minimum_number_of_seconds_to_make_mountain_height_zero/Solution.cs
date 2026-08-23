// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

public class Solution {
    public long MinNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        bool Ok(long t) {
            long total = 0;
            foreach (int w in workerTimes) {
                long lo = 0, hi = mountainHeight;
                while (lo < hi) {
                    long mid = (lo + hi + 1) / 2;
                    if ((long)w * mid * (mid + 1) / 2 <= t) lo = mid;
                    else hi = mid - 1;
                }
                total += lo;
                if (total >= mountainHeight) return true;
            }
            return total >= mountainHeight;
        }
        long lo = 0, hi = (long)1e18;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
