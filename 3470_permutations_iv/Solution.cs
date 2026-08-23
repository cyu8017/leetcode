// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] Permute(int n, long k) {
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i;
            if (fact[i] > (long)1e18) fact[i] = (long)1e18 + 1;
        }
        bool[] used = new bool[n + 1];
        var ans = new List<int>();
        bool Dfs(int pos) {
            if (pos == n) return true;
            for (int x = 1; x <= n; x++) {
                if (used[x]) continue;
                if (pos > 0 && (ans[pos - 1] % 2 == x % 2)) continue;
                int rem = n - pos - 1;
                long cnt = fact[rem];
                if (cnt >= k) {
                    used[x] = true;
                    ans.Add(x);
                    if (Dfs(pos + 1)) return true;
                    ans.RemoveAt(ans.Count - 1);
                    used[x] = false;
                } else {
                    k -= cnt;
                }
            }
            return false;
        }
        if (!Dfs(0)) return Array.Empty<int>();
        return ans.ToArray();
    }
}
