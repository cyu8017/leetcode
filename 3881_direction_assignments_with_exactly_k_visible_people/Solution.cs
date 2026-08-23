// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

using System;

public class Solution {
    const int N = 100001;
    const int MOD = 1000000007;
    static long[] fact;
    static long[] invFact;
    static bool ready = false;

    static long Qmi(long a, long k, long p) {
        long res = 1;
        while (k != 0) {
            if ((k & 1) != 0) res = res * a % p;
            k >>= 1;
            a = a * a % p;
        }
        return res;
    }

    static void Init() {
        if (ready) return;
        fact = new long[N];
        invFact = new long[N];
        fact[0] = invFact[0] = 1;
        for (int i = 1; i < N; i++) {
            fact[i] = fact[i - 1] * i % MOD;
            invFact[i] = Qmi(fact[i], MOD - 2, MOD);
        }
        ready = true;
    }

    static long Comb(int n, int k) {
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }

    public int CountVisiblePeople(int n, int pos, int k) {
        Init();
        int l = pos, r = n - pos - 1;
        long ans = 0;
        for (int a = 0; a <= Math.Min(k, l); a++) {
            int b = k - a;
            if (b <= r) {
                ans = (ans + 2 * Comb(l, a) % MOD * Comb(r, b) % MOD) % MOD;
            }
        }
        return (int)ans;
    }
}
