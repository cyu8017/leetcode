// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        long sum = 0;
        foreach (int b in batteries) sum += b;
        long lo = 1, hi = sum / n;
        bool Can(long t) {
            long need = 0;
            foreach (int b in batteries) need += Math.Min((long)b, t);
            return need >= t * n;
        }
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (Can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
