// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

using System;
using System.Collections.Generic;

public class Solution {
    static int Popcount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public int MaxPartitionsAfterOperations(string s, int k) {
        int n = s.Length;
        var memo = new Dictionary<long, int>();
        long Key(int i, int cur, int t) => ((long)i << 32) | ((long)cur << 1) | t;
        int Dfs(int i, int cur, int t) {
            if (i >= n) return 1;
            long kkey = Key(i, cur, t);
            if (memo.TryGetValue(kkey, out int cached)) return cached;
            int v = 1 << (s[i] - 'a');
            int nxt = cur | v;
            int ans;
            if (Popcount(nxt) > k) ans = Dfs(i + 1, v, t) + 1;
            else ans = Dfs(i + 1, nxt, t);
            if (t > 0) {
                for (int j = 0; j < 26; j++) {
                    nxt = cur | (1 << j);
                    if (Popcount(nxt) > k)
                        ans = Math.Max(ans, Dfs(i + 1, 1 << j, 0) + 1);
                    else
                        ans = Math.Max(ans, Dfs(i + 1, nxt, 0));
                }
            }
            return memo[kkey] = ans;
        }
        return Dfs(0, 0, 1);
    }
}
