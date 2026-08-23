// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

using System.Collections.Generic;

public class Solution {
    static int ModPow(long a, long e, int mod) {
        long r = 1;
        a %= mod;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int)r;
    }

    public int CountBalancedPermutations(string num) {
        const int mod = 1000000007;
        int[] cnt = new int[10];
        int sum = 0;
        foreach (char c in num) {
            cnt[c - '0']++;
            sum += c - '0';
        }
        if (sum % 2 == 1) return 0;
        int n = num.Length;
        int halfN = n / 2, halfS = sum / 2;
        int[] fact = new int[n + 1], invF = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = (int)((long)fact[i - 1] * i % mod);
        invF[n] = ModPow(fact[n], mod - 2, mod);
        for (int i = n; i > 0; i--) invF[i - 1] = (int)((long)invF[i] * i % mod);

        var dp = new Dictionary<(int, int), int>();
        dp[(0, 0)] = 1;
        for (int d = 0; d <= 9; d++) {
            var ndp = new Dictionary<(int, int), int>();
            foreach (var kv in dp) {
                int used = kv.Key.Item1, s = kv.Key.Item2, ways = kv.Value;
                for (int take = 0; take <= cnt[d]; take++) {
                    int nu = used + take, ns = s + take * d;
                    if (nu > halfN || ns > halfS) continue;
                    int w = (int)((long)ways * invF[take] % mod * invF[cnt[d] - take] % mod);
                    var key = (nu, ns);
                    if (!ndp.ContainsKey(key)) ndp[key] = 0;
                    ndp[key] = (ndp[key] + w) % mod;
                }
            }
            dp = ndp;
        }
        int ans = dp.TryGetValue((halfN, halfS), out int v) ? v : 0;
        ans = (int)((long)ans * fact[halfN] % mod * fact[n - halfN] % mod);
        for (int d = 0; d <= 9; d++) ans = (int)((long)ans * fact[cnt[d]] % mod);
        return ans;
    }
}
