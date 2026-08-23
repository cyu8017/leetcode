// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private String s;
    private int k, n;
    private Map<Long, Integer> memo;

    private static int popcount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    private long key(int i, int cur, int t) {
        return ((long) i << 32) | ((long) cur << 1) | t;
    }

    private int dfs(int i, int cur, int t) {
        if (i >= n) return 1;
        long kkey = key(i, cur, t);
        if (memo.containsKey(kkey)) return memo.get(kkey);
        int v = 1 << (s.charAt(i) - 'a');
        int nxt = cur | v;
        int ans;
        if (popcount(nxt) > k) ans = dfs(i + 1, v, t) + 1;
        else ans = dfs(i + 1, nxt, t);
        if (t > 0) {
            for (int j = 0; j < 26; j++) {
                nxt = cur | (1 << j);
                if (popcount(nxt) > k)
                    ans = Math.max(ans, dfs(i + 1, 1 << j, 0) + 1);
                else
                    ans = Math.max(ans, dfs(i + 1, nxt, 0));
            }
        }
        memo.put(kkey, ans);
        return ans;
    }

    public int maxPartitionsAfterOperations(String s, int k) {
        this.s = s;
        this.k = k;
        this.n = s.length();
        this.memo = new HashMap<>();
        return dfs(0, 0, 1);
    }
}
