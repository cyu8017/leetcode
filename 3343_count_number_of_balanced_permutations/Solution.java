// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static int modPow(long a, long e, int mod) {
        long r = 1;
        a %= mod;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int) r;
    }

    private static long key(int a, int b) {
        return ((long) a << 32) | (b & 0xffffffffL);
    }

    public int countBalancedPermutations(String num) {
        final int mod = 1_000_000_007;
        int[] cnt = new int[10];
        int sum = 0;
        for (char c : num.toCharArray()) {
            cnt[c - '0']++;
            sum += c - '0';
        }
        if (sum % 2 == 1) return 0;
        int n = num.length();
        int halfN = n / 2, halfS = sum / 2;
        int[] fact = new int[n + 1], invF = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = (int) ((long) fact[i - 1] * i % mod);
        invF[n] = modPow(fact[n], mod - 2, mod);
        for (int i = n; i > 0; i--) invF[i - 1] = (int) ((long) invF[i] * i % mod);

        Map<Long, Integer> dp = new HashMap<>();
        dp.put(key(0, 0), 1);
        for (int d = 0; d <= 9; d++) {
            Map<Long, Integer> ndp = new HashMap<>();
            for (Map.Entry<Long, Integer> kv : dp.entrySet()) {
                long st = kv.getKey();
                int used = (int) (st >> 32), s = (int) st;
                int ways = kv.getValue();
                for (int take = 0; take <= cnt[d]; take++) {
                    int nu = used + take, ns = s + take * d;
                    if (nu > halfN || ns > halfS) continue;
                    int w = (int) ((long) ways * invF[take] % mod * invF[cnt[d] - take] % mod);
                    long nk = key(nu, ns);
                    ndp.put(nk, (ndp.getOrDefault(nk, 0) + w) % mod);
                }
            }
            dp = ndp;
        }
        int ans = dp.getOrDefault(key(halfN, halfS), 0);
        ans = (int) ((long) ans * fact[halfN] % mod * fact[n - halfN] % mod);
        for (int d = 0; d <= 9; d++) ans = (int) ((long) ans * fact[cnt[d]] % mod);
        return ans;
    }
}
