// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

using System;
using System.Collections.Generic;

public class Solution {
    class Hashing {
        long[] p, h;
        long mod;
        public Hashing(string word, long bas, long mod) {
            this.mod = mod;
            int n = word.Length;
            p = new long[n + 1];
            h = new long[n + 1];
            p[0] = 1;
            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * bas % mod;
                h[i] = (h[i - 1] * bas + word[i - 1]) % mod;
            }
        }
        public long Query(int l, int r) {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
        }
    }

    public int MinimumCost(string target, string[] words, int[] costs) {
        const long bas = 13331, mod = 998244353;
        const int inf = int.MaxValue / 2;
        int n = target.Length;
        var hashing = new Hashing(target, bas, mod);
        int[] f = new int[n + 1];
        Array.Fill(f, inf);
        f[0] = 0;
        var ss = new HashSet<int>();
        foreach (var w in words) ss.Add(w.Length);
        var lengths = new List<int>(ss);
        lengths.Sort();
        var d = new Dictionary<long, int>();
        for (int i = 0; i < words.Length; i++) {
            long x = 0;
            foreach (char c in words[i]) x = (x * bas + c) % mod;
            if (!d.ContainsKey(x) || costs[i] < d[x]) d[x] = costs[i];
        }
        for (int i = 1; i <= n; i++) {
            foreach (int j in lengths) {
                if (j > i) break;
                long x = hashing.Query(i - j + 1, i);
                if (d.ContainsKey(x)) f[i] = Math.Min(f[i], f[i - j] + d[x]);
            }
        }
        return f[n] >= inf ? -1 : f[n];
    }
}
