// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution {
    public int smallestValue(int n) {
        while (true) {
            int s = SumPrimeFactors(n);
            if (s == n) return n;
            n = s;
        }
    }

    private int sumPrimeFactors(int x) {
        int s = 0;
        for (int i = 2; i * i <= x; i++) {
            while (x % i == 0) {
                s += i;
                x /= i;
            }
        }
        if (x > 1) s += x;
        return s;
    }
}
