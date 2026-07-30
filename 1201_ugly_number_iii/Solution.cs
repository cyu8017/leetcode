// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

using System;

public class Solution {
    public int NthUglyNumber(int n, int a, int b, int c) {
        long Lcm(long x, long y) => x / Gcd(x, y) * y;
        long ab = Lcm(a, b), ac = Lcm(a, c), bc = Lcm(b, c), abc = Lcm(ab, c);

        long Count(long x) => x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;

        long lo = 1, hi = 2_000_000_000;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (Count(mid) >= n) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }

    private static long Gcd(long x, long y) {
        while (y != 0) (x, y) = (y, x % y);
        return x;
    }
}
