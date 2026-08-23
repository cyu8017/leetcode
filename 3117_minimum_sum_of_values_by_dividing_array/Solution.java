// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int INF = 1 << 29;
    private int[] nums;
    private int[] andValues;
    private int n, m;
    private Map<Long, Integer> f;

    private int dfs(int i, int j, int a) {
        if (n - i < m - j) return INF;
        if (j == m) return i == n ? 0 : INF;
        a &= nums[i];
        if (a < andValues[j]) return INF;
        long key = ((long) i << 36) | ((long) j << 32) | (a & 0xffffffffL);
        Integer cached = f.get(key);
        if (cached != null) return cached;
        int ans = dfs(i + 1, j, a);
        if (a == andValues[j]) {
            ans = Math.min(ans, dfs(i + 1, j + 1, -1) + nums[i]);
        }
        f.put(key, ans);
        return ans;
    }

    public int minimumValueSum(int[] nums, int[] andValues) {
        this.nums = nums;
        this.andValues = andValues;
        this.n = nums.length;
        this.m = andValues.length;
        this.f = new HashMap<>();
        int ans = dfs(0, 0, -1);
        return ans < INF ? ans : -1;
    }
}
