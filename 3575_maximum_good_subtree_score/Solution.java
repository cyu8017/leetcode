// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    static final int MOD = 1_000_000_007;
    List<Integer>[] g;
    int[] vals;
    int ans;

    int[] digitMask(int x) {
        int v = x, mask = 0;
        if (x == 0) return new int[] {1, 1, 0};
        while (x > 0) {
            int d = x % 10;
            if ((mask & (1 << d)) != 0) return new int[] {0, 0, 0};
            mask |= 1 << d;
            x /= 10;
        }
        return new int[] {mask, 1, v};
    }

    Map<Integer, Integer> dfs(int u) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);
        int[] dm = digitMask(vals[u]);
        if (dm[1] == 1) dp.put(dm[0], dm[2]);
        for (int c : g[u]) {
            Map<Integer, Integer> child = dfs(c);
            Map<Integer, Integer> ndp = new HashMap<>();
            for (Map.Entry<Integer, Integer> e1 : dp.entrySet()) {
                for (Map.Entry<Integer, Integer> e2 : child.entrySet()) {
                    if ((e1.getKey() & e2.getKey()) == 0) {
                        int nm = e1.getKey() | e2.getKey();
                        ndp.put(nm, Math.max(ndp.getOrDefault(nm, 0), e1.getValue() + e2.getValue()));
                    }
                }
            }
            for (Map.Entry<Integer, Integer> e : dp.entrySet())
                ndp.put(e.getKey(), Math.max(ndp.getOrDefault(e.getKey(), 0), e.getValue()));
            for (Map.Entry<Integer, Integer> e : child.entrySet())
                ndp.put(e.getKey(), Math.max(ndp.getOrDefault(e.getKey(), 0), e.getValue()));
            dp = ndp;
        }
        int best = 0;
        for (int s : dp.values()) best = Math.max(best, s);
        ans = (ans + best) % MOD;
        return dp;
    }

    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        this.vals = vals;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) g[par[i]].add(i);
        ans = 0;
        dfs(0);
        return ans;
    }
}
