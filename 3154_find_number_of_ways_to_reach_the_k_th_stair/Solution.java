// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int k;
    private Map<Long, Integer> f;

    private int dfs(long i, int j, int jump) {
        if (i > k + 1) return 0;
        long key = (i << 32) | ((long) jump << 1) | j;
        Integer cached = f.get(key);
        if (cached != null) return cached;
        int ans = 0;
        if (i == k) ans++;
        if (i > 0 && j == 0) ans += dfs(i - 1, 1, jump);
        ans += dfs(i + (1L << jump), 0, jump + 1);
        f.put(key, ans);
        return ans;
    }

    public int waysToReachStair(int k) {
        this.k = k;
        this.f = new HashMap<>();
        return dfs(1, 0, 0);
    }
}
