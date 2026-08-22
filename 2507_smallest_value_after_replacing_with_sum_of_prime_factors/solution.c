// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

static int sumPrimeFactors(int x) {
    int s = 0;
    for (int i = 2; i * i <= x; i++) {
        while (x % i == 0) { s += i; x /= i; }
    }
    if (x > 1) s += x;
    return s;
}

int smallestValue(int n) {
    for (;;) {
        int s = sumPrimeFactors(n);
        if (s == n) return n;
        n = s;
    }
}
