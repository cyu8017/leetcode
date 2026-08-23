// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

class Solution {
    private static final int N = 100001;
    private static final int MOD = 1000000007;
    private static long[] fact;
    private static long[] invFact;
    private static boolean ready = false;

    private static long qmi(long a, long k, long p) {
        long res = 1;
        while (k != 0) {
            if ((k & 1) != 0) res = res * a % p;
            k >>= 1;
            a = a * a % p;
        }
        return res;
    }

    private static void init() {
        if (ready) return;
        fact = new long[N];
        invFact = new long[N];
        fact[0] = invFact[0] = 1;
        for (int i = 1; i < N; i++) {
            fact[i] = fact[i - 1] * i % MOD;
            invFact[i] = qmi(fact[i], MOD - 2, MOD);
        }
        ready = true;
    }

    private static long comb(int n, int k) {
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }

    public int countVisiblePeople(int n, int pos, int k) {
        init();
        int l = pos, r = n - pos - 1;
        long ans = 0;
        for (int a = 0; a <= Math.min(k, l); a++) {
            int b = k - a;
            if (b <= r) {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD;
            }
        }
        return (int) ans;
    }
}
