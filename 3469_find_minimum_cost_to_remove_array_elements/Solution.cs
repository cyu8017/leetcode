// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

using System;
using System.Collections.Generic;

public class Solution {
    Dictionary<(int, int), int> memo = new();
    int[] nums;
    int n;
    int Max2(int a, int b) => a > b ? a : b;
    int Min3(int a, int b, int c) => Math.Min(a, Math.Min(b, c));
    int Dfs(int i, int prev) {
        if (i >= n) return prev == -1 ? 0 : nums[prev];
        var key = (i, prev);
        if (memo.TryGetValue(key, out int cached)) return cached;
        int res;
        if (prev == -1) {
            if (i + 1 >= n) res = nums[i];
            else if (i + 2 >= n) res = Max2(nums[i], nums[i + 1]);
            else {
                int a = nums[i], b = nums[i + 1], c = nums[i + 2];
                res = Min3(Max2(b, c) + Dfs(i + 3, i), Max2(a, c) + Dfs(i + 3, i + 1), Max2(a, b) + Dfs(i + 3, i + 2));
            }
        } else {
            if (i + 1 >= n) res = Max2(nums[prev], nums[i]);
            else {
                int a = nums[prev], b = nums[i], c = nums[i + 1];
                res = Min3(Max2(b, c) + Dfs(i + 2, prev), Max2(a, c) + Dfs(i + 2, i), Max2(a, b) + Dfs(i + 2, i + 1));
            }
        }
        return memo[key] = res;
    }

    public int MinCost(int[] nums_) {
        nums = nums_;
        n = nums.Length;
        memo.Clear();
        return Dfs(0, -1);
    }
}
