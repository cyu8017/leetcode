struct Solution;
// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

impl Solution {
    pub fn max_a(n: i32) -> i32 {
        let n = n as usize;
        let mut dp: Vec<i32> = (0..=n as i32).collect();
        for i in 1..=n {
            for j in 0..i.saturating_sub(2) {
                dp[i] = dp[i].max(dp[j] * (i - j - 1) as i32);
            }
        }
        dp[n]
    }
}

fn main() {}
