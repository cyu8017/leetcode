// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![vec![0; n]; n];
        for index in 0..n {
            dp[index][index] = nums[index];
        }
        for length in 2..=n {
            for left in 0..=n - length {
                let right = left + length - 1;
                dp[left][right] =
                    (nums[left] - dp[left + 1][right]).max(nums[right] - dp[left][right - 1]);
            }
        }
        dp[0][n - 1] >= 0
    }
}
