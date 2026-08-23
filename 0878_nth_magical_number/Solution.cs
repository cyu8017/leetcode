// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

using System;

public class Solution {
    public int NthMagicalNumber(int n, int a, int b) {
        const int MOD = 1_000_000_007;
        long Gcd(long x, long y) {
            while (y != 0) { long t = x % y; x = y; y = t; }
            return x;
        }
        long lcm = (long)a / Gcd(a, b) * b;
        long lo = 1, hi = (long)n * Math.Min(a, b);
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (mid / a + mid / b - mid / lcm >= n) hi = mid;
            else lo = mid + 1;
        }
        return (int)(lo % MOD);
    }
}
