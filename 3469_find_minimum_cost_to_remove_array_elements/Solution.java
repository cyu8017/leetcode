// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private final Map<Long, Integer> memo = new HashMap<>();
    private int[] nums;
    private int n;

    private int max2(int a, int b) { return a > b ? a : b; }
    private int min3(int a, int b, int c) { return Math.min(a, Math.min(b, c)); }

    private long key(int i, int prev) { return ((long) i << 32) | (prev & 0xffffffffL); }

    private int dfs(int i, int prev) {
        if (i >= n) return prev == -1 ? 0 : nums[prev];
        long k = key(i, prev);
        Integer cached = memo.get(k);
        if (cached != null) return cached;
        int res;
        if (prev == -1) {
            if (i + 1 >= n) res = nums[i];
            else if (i + 2 >= n) res = max2(nums[i], nums[i + 1]);
            else {
                int a = nums[i], b = nums[i + 1], c = nums[i + 2];
                res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2));
            }
        } else {
            if (i + 1 >= n) res = max2(nums[prev], nums[i]);
            else {
                int a = nums[prev], b = nums[i], c = nums[i + 1];
                res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1));
            }
        }
        memo.put(k, res);
        return res;
    }

    public int minCost(int[] nums) {
        this.nums = nums;
        n = nums.length;
        memo.clear();
        return dfs(0, -1);
    }
}
