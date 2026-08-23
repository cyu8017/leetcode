// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

using System;

public class Solution {
    public long MaxPower(int[] stations, int r, int k) {
        int n = stations.Length;
        long[] diff = new long[n + 1];
        for (int i = 0; i < n; i++) {
            int L = Math.Max(0, i - r);
            int R = Math.Min(n - 1, i + r);
            diff[L] += stations[i];
            diff[R + 1] -= stations[i];
        }
        long[] power = new long[n];
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            power[i] = cur;
        }

        bool Ok(long x) {
            long[] extra = new long[n + 1];
            long have = 0, used = 0;
            for (int i = 0; i < n; i++) {
                have += extra[i];
                long need = x - (power[i] + have);
                if (need > 0) {
                    used += need;
                    if (used > k) return false;
                    have += need;
                    int end = i + 2 * r;
                    if (end + 1 <= n) extra[end + 1] -= need;
                }
            }
            return true;
        }

        long lo = 0, hi = k;
        foreach (long p in power) if (p > hi) hi = p;
        hi += k;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
