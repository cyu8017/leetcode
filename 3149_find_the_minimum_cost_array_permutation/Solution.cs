// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindPermutation(int[] nums) {
        int n = nums.Length;
        int[][] memo = new int[1 << n][];
        for (int i = 0; i < memo.Length; i++) {
            memo[i] = new int[n];
            for (int j = 0; j < n; j++) memo[i][j] = -1;
        }
        int Absv(int x) => x < 0 ? -x : x;
        int Dfs(int mask, int pre) {
            if (mask == (1 << n) - 1) return Absv(pre - nums[0]);
            if (memo[mask][pre] != -1) return memo[mask][pre];
            int res = int.MaxValue;
            for (int cur = 1; cur < n; cur++) {
                if (((mask >> cur) & 1) == 0) {
                    res = Math.Min(res, Absv(pre - nums[cur]) + Dfs(mask | (1 << cur), cur));
                }
            }
            return memo[mask][pre] = res;
        }
        var ans = new List<int>();
        void G(int mask, int pre) {
            ans.Add(pre);
            if (mask == (1 << n) - 1) return;
            int res = Dfs(mask, pre);
            for (int cur = 1; cur < n; cur++) {
                if (((mask >> cur) & 1) == 0) {
                    if (Absv(pre - nums[cur]) + Dfs(mask | (1 << cur), cur) == res) {
                        G(mask | (1 << cur), cur);
                        break;
                    }
                }
            }
        }
        G(1, 0);
        return ans.ToArray();
    }
}
