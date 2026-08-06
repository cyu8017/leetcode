// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

impl Solution {
    pub fn num_subseq(mut nums: Vec<i32>, target: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        nums.sort_unstable();
        let mut powers = vec![1; nums.len() + 1];
        for i in 1..powers.len() {
            powers[i] = (powers[i - 1] * 2) % MOD;
        }
        let mut left = 0usize;
        let mut right = nums.len() - 1;
        let mut ans = 0;
        while left <= right {
            if nums[left] + nums[right] <= target {
                ans = (ans + powers[right - left]) % MOD;
                left += 1;
            } else {
                if right == 0 {
                    break;
                }
                right -= 1;
            }
        }
        ans
    }
}
