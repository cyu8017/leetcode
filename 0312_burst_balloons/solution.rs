// LeetCode 0312 - Burst Balloons
// https://leetcode.com/problems/burst-balloons/

impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let mut balloons = Vec::with_capacity(nums.len() + 2);
        balloons.push(1);
        balloons.extend(nums);
        balloons.push(1);

        let size = balloons.len();
        let mut dp = vec![vec![0; size]; size];

        for length in 3..=size {
            for left in 0..=size - length {
                let right = left + length - 1;
                for mid in left + 1..right {
                    let coins = dp[left][mid]
                        + dp[mid][right]
                        + balloons[left] * balloons[mid] * balloons[right];
                    dp[left][right] = dp[left][right].max(coins);
                }
            }
        }

        dp[0][size - 1]
    }
}
