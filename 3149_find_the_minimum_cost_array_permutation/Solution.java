// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int[] nums;
    private int n;
    private int[][] memo;
    private List<Integer> ans;

    private int absv(int x) {
        return x < 0 ? -x : x;
    }

    private int dfs(int mask, int pre) {
        if (mask == (1 << n) - 1) return absv(pre - nums[0]);
        if (memo[mask][pre] != -1) return memo[mask][pre];
        int res = Integer.MAX_VALUE;
        for (int cur = 1; cur < n; cur++) {
            if (((mask >> cur) & 1) == 0) {
                res = Math.min(res, absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur));
            }
        }
        return memo[mask][pre] = res;
    }

    private void g(int mask, int pre) {
        ans.add(pre);
        if (mask == (1 << n) - 1) return;
        int res = dfs(mask, pre);
        for (int cur = 1; cur < n; cur++) {
            if (((mask >> cur) & 1) == 0) {
                if (absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur) == res) {
                    g(mask | (1 << cur), cur);
                    break;
                }
            }
        }
    }

    public int[] findPermutation(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        this.memo = new int[1 << n][n];
        for (int[] row : memo) Arrays.fill(row, -1);
        this.ans = new ArrayList<>();
        g(1, 0);
        int[] out = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) out[i] = ans.get(i);
        return out;
    }
}
