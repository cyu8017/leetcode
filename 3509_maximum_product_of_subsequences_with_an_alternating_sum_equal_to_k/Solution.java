// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    static final int MIN = -5000;
    Map<String, Integer> memo;
    int[] nums;
    int limit;

    int dp(int i, int product, int state, int kk) {
        if (i == nums.length) {
            if (kk == 0 && state != 0 && product <= limit) return product;
            return MIN;
        }
        String key = i + "," + product + "," + state + "," + kk;
        if (memo.containsKey(key)) return memo.get(key);
        int res = dp(i + 1, product, state, kk);
        if (state == 0) res = Math.max(res, dp(i + 1, nums[i], 1, kk - nums[i]));
        if (state == 1) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.max(res, dp(i + 1, np, 2, kk + nums[i]));
        }
        if (state == 2) {
            int np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.max(res, dp(i + 1, np, 1, kk - nums[i]));
        }
        memo.put(key, res);
        return res;
    }

    public int maxProduct(int[] nums_, int k, int limit_) {
        nums = nums_;
        limit = limit_;
        memo = new HashMap<>();
        int sumAll = 0;
        for (int v : nums) sumAll += v;
        if (Math.abs(k) > sumAll) return -1;
        int ans = dp(0, 1, 0, k);
        return ans == MIN ? -1 : ans;
    }
}
