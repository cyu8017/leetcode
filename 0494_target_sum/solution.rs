// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let total: i64 = nums.iter().map(|value| *value as i64).sum();
        if (total + target as i64) % 2 != 0 || target.unsigned_abs() as i64 > total {
            return 0;
        }
        let need = ((total + target as i64) / 2) as usize;
        let mut dp = vec![0i64; need + 1];
        dp[0] = 1;
        for num in nums {
            let num = num as usize;
            for amount in (num..=need).rev() {
                dp[amount] += dp[amount - num];
            }
        }
        dp[need] as i32
    }
}
