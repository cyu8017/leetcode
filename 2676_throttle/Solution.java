// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

// JS throttle stand-in: calls fn at most once per t ms (wall clock)
class Solution {
    public Runnable throttle(Runnable fn, int t) {
        long[] last = new long[] {System.nanoTime() - 24L * 3600 * 1_000_000_000L};
        return () -> {
            long now = System.nanoTime();
            if ((now - last[0]) / 1_000_000L >= t) {
                last[0] = now;
                fn.run();
            }
        };
    }
}
