// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution {
    public long maxRunTime(int n, int[] batteries) {
        long sum = 0;
        for (int b : batteries) sum += b;
        long lo = 1, hi = sum / n;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            long need = 0;
            for (int b : batteries) need += Math.min((long) b, mid);
            if (need >= mid * n) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
