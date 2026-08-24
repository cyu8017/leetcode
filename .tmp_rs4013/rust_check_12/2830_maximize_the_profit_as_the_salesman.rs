struct Solution;
// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

impl Solution {
    pub fn maximize_the_profit(n: i32, offers: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut by_end = vec![Vec::new(); n];
        for o in offers {
            by_end[o[1] as usize].push(o);
        }
        let mut dp = vec![0i32; n + 1];
        for end in 0..n {
            dp[end + 1] = dp[end];
            for o in &by_end[end] {
                dp[end + 1] = dp[end + 1].max(dp[o[0] as usize] + o[2]);
            }
        }
        dp[n]
    }
}

fn main() {}
