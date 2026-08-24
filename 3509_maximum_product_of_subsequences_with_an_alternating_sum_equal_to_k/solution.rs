// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

use std::collections::HashMap;

impl Solution {
    const MIN: i32 = -5000;

    fn dp(
        i: usize,
        product: i32,
        state: i32,
        kk: i32,
        nums: &[i32],
        limit: i32,
        memo: &mut HashMap<(usize, i32, i32, i32), i32>,
    ) -> i32 {
        if i == nums.len() {
            if kk == 0 && state != 0 && product <= limit {
                return product;
            }
            return Self::MIN;
        }
        let key = (i, product, state, kk);
        if let Some(&v) = memo.get(&key) {
            return v;
        }
        let mut res = Self::dp(i + 1, product, state, kk, nums, limit, memo);
        if state == 0 {
            res = res.max(Self::dp(i + 1, nums[i], 1, kk - nums[i], nums, limit, memo));
        }
        if state == 1 {
            let mut np = product * nums[i];
            if np > limit + 1 {
                np = limit + 1;
            }
            res = res.max(Self::dp(i + 1, np, 2, kk + nums[i], nums, limit, memo));
        }
        if state == 2 {
            let mut np = product * nums[i];
            if np > limit + 1 {
                np = limit + 1;
            }
            res = res.max(Self::dp(i + 1, np, 1, kk - nums[i], nums, limit, memo));
        }
        memo.insert(key, res);
        res
    }

    pub fn max_product(nums: Vec<i32>, k: i32, limit: i32) -> i32 {
        let sum_all: i32 = nums.iter().sum();
        if k.abs() > sum_all {
            return -1;
        }
        let mut memo = HashMap::new();
        let ans = Self::dp(0, 1, 0, k, &nums, limit, &mut memo);
        if ans == Self::MIN { -1 } else { ans }
    }
}
