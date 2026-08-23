// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

public class Solution {
    public int NumberOfSequence(int n, int[] sick) {
        const int mod = 1000000007;
        int[] fact = new int[n + 1], invFact = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = (int)(1L * fact[i - 1] * i % mod);
        int ModPow(long a, int b) {
            long res = 1;
            while (b > 0) {
                if ((b & 1) != 0) res = res * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)res;
        }
        invFact[n] = ModPow(fact[n], mod - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = (int)(1L * invFact[i] * i % mod);
        int m = sick.Length;
        int totalEmpty = n - m;
        long ans = fact[totalEmpty];
        int prev = -1;
        foreach (int s in sick) {
            int gap = s - prev - 1;
            if (prev == -1) ans = ans * invFact[gap] % mod;
            else if (gap > 0) ans = ans * invFact[gap] % mod * ModPow(2, gap - 1) % mod;
            prev = s;
        }
        int gap2 = n - prev - 1;
        ans = ans * invFact[gap2] % mod;
        return (int)ans;
    }
}
