// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

class Solution {
    private static final int MOD = 1_000_000_007;

    private int modPow(long a, int b) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return (int) res;
    }

    public int numberOfSequence(int n, int[] sick) {
        int[] fact = new int[n + 1], invFact = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = (int) (1L * fact[i - 1] * i % MOD);
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = (int) (1L * invFact[i] * i % MOD);
        int m = sick.length;
        int totalEmpty = n - m;
        long ans = fact[totalEmpty];
        int prev = -1;
        for (int s : sick) {
            int gap = s - prev - 1;
            if (prev == -1) ans = ans * invFact[gap] % MOD;
            else if (gap > 0) ans = ans * invFact[gap] % MOD * modPow(2, gap - 1) % MOD;
            prev = s;
        }
        int gap2 = n - prev - 1;
        ans = ans * invFact[gap2] % MOD;
        return (int) ans;
    }
}
