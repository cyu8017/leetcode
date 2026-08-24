// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

impl Solution {
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {
        let mut dp = [0i32; 26];
        let mut ans = 0;
        for ch in s.bytes() {
            let c = (ch - b'a') as i32;
            let mut best = 0;
            for p in 0..26 {
                if (c - p).abs() <= k && dp[p as usize] > best {
                    best = dp[p as usize];
                }
            }
            dp[c as usize] = best + 1;
            ans = ans.max(dp[c as usize]);
        }
        ans
    }
}
