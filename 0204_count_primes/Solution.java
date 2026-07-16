// LeetCode 0204 - Count Primes\n// https://leetcode.com/problems/\n\nclass Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;
        boolean[] prime = new boolean[n];
        java.util.Arrays.fill(prime, true);
        for (int p = 2; p * p < n; p++) {
            if (prime[p]) for (int multiple = p * p; multiple < n; multiple += p) prime[multiple] = false;
        }
        int count = 0;
        for (int i = 2; i < n; i++) if (prime[i]) count++;
        return count;
    }
}
