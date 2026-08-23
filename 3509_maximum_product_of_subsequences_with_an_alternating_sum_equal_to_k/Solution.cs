// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

using System;
using System.Collections.Generic;

public class Solution {
    const int MIN = -5000;
    Dictionary<(int, int, int, int), int> memo;
    int[] nums;
    int limit;

    int Dp(int i, int product, int state, int kk) {
        if (i == nums.Length) {
            if (kk == 0 && state != 0 && product <= limit) return product;
            return MIN;
        }
        var key = (i, product, state, kk);
        if (memo.ContainsKey(key)) return memo[key];
        int res = Dp(i + 1, product, state, kk);
        if (state == 0) res = Math.Max(res, Dp(i + 1, nums[i], 1, kk - nums[i]));
        if (state == 1) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.Max(res, Dp(i + 1, np, 2, kk + nums[i]));
        }
        if (state == 2) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.Max(res, Dp(i + 1, np, 1, kk - nums[i]));
        }
        return memo[key] = res;
    }

    public int MaxProduct(int[] nums_, int k, int limit_) {
        nums = nums_;
        limit = limit_;
        memo = new Dictionary<(int, int, int, int), int>();
        int sumAll = 0;
        foreach (int v in nums) sumAll += v;
        if (Math.Abs(k) > sumAll) return -1;
        int ans = Dp(0, 1, 0, k);
        return ans == MIN ? -1 : ans;
    }
}
