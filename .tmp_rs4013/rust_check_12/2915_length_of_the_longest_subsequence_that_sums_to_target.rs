struct Solution;
// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

impl Solution {
    pub fn length_of_longest_subsequence(nums: Vec<i32>, target: i32) -> i32 {
        let target = target as usize;
        let mut dp = vec![-1i32; target + 1];
        dp[0] = 0;
        for v in nums {
            let v = v as usize;
            for s in (v..=target).rev() {
                if dp[s - v] >= 0 && dp[s - v] + 1 > dp[s] {
                    dp[s] = dp[s - v] + 1;
                }
            }
        }
        dp[target]
    }
}

fn main() {}
