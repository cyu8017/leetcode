struct Solution;
// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 1;
        let mut dp = vec![vec![0; 301]; n];
        for i in 0..n {
            for j in 0..i {
                let d = (nums[i] - nums[j]).unsigned_abs() as usize;
                let mut best = 1;
                for pd in d..=300 {
                    if dp[j][pd] > best {
                        best = dp[j][pd];
                    }
                }
                if best + 1 > dp[i][d] {
                    dp[i][d] = best + 1;
                }
                if dp[i][d] > ans {
                    ans = dp[i][d];
                }
            }
            if dp[i][0] < 1 {
                dp[i][0] = 1;
            }
        }
        ans
    }
}

fn main() {}
