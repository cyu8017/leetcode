// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private long[] fact;
    private boolean[] used;
    private List<Integer> ans;
    private long k;
    private int n;

    public int[] permute(int n, long k) {
        this.n = n;
        this.k = k;
        fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i;
            if (fact[i] > (long) 1e18) fact[i] = (long) 1e18 + 1;
        }
        used = new boolean[n + 1];
        ans = new ArrayList<>();
        if (!dfs(0)) return new int[0];
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }

    private boolean dfs(int pos) {
        if (pos == n) return true;
        for (int x = 1; x <= n; x++) {
            if (used[x]) continue;
            if (pos > 0 && (ans.get(pos - 1) % 2 == x % 2)) continue;
            int rem = n - pos - 1;
            long cnt = fact[rem];
            if (cnt >= k) {
                used[x] = true;
                ans.add(x);
                if (dfs(pos + 1)) return true;
                ans.remove(ans.size() - 1);
                used[x] = false;
            } else {
                k -= cnt;
            }
        }
        return false;
    }
}
