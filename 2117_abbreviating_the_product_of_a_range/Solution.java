// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

class Solution {
    public String abbreviateProduct(int left, int right) {
        int twos = 0, fives = 0;
        for (int i = left; i <= right; i++) {
            int x = i;
            while (x % 2 == 0) { twos++; x /= 2; }
            while (x % 5 == 0) { fives++; x /= 5; }
        }
        int zeros = Math.min(twos, fives);
        final long MOD = 100000000000L;
        long prod = 1;
        int extra2 = twos - zeros, extra5 = fives - zeros;
        double logSum = 0.0;
        for (int i = left; i <= right; i++) {
            int x = i;
            while (x % 2 == 0) x /= 2;
            while (x % 5 == 0) x /= 5;
            prod = (prod * x) % MOD;
            logSum += Math.log10(x);
        }
        for (int i = 0; i < extra2; i++) { prod = (prod * 2) % MOD; logSum += Math.log10(2.0); }
        for (int i = 0; i < extra5; i++) { prod = (prod * 5) % MOD; logSum += Math.log10(5.0); }
        double fullLog = 0.0;
        for (int i = left; i <= right; i++) fullLog += Math.log10(i);
        int digits = (int) fullLog + 1;
        if (digits <= 10) {
            long p = 1;
            for (int i = left; i <= right; i++) p *= i;
            return Long.toString(p);
        }
        double frac = logSum - Math.floor(logSum);
        long prefix = (long) Math.pow(10.0, frac + 4);
        long suffix = prod % 100000;
        return prefix + "e" + zeros + String.format("%05d", suffix);
    }
}
