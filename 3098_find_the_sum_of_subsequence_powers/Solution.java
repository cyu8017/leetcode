// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[] nums;
    private int n;
    private Map<Long, Integer> f;

    private int dfs(int i, int j, int kk, int mi) {
        if (i >= n) return kk == 0 ? mi : 0;
        if (n - i < kk) return 0;
        long key = ((long) mi << 18) | ((long) i << 12) | ((long) j << 6) | kk;
        Integer cached = f.get(key);
        if (cached != null) return cached;
        int ans = dfs(i + 1, j, kk, mi);
        if (j == n) ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD;
        else ans = (ans + dfs(i + 1, i, kk - 1, Math.min(mi, nums[i] - nums[j]))) % MOD;
        f.put(key, ans);
        return ans;
    }

    public int sumOfPowers(int[] nums, int k) {
        Arrays.sort(nums);
        this.nums = nums;
        this.n = nums.length;
        this.f = new HashMap<>();
        return dfs(0, n, k, Integer.MAX_VALUE);
    }
}
