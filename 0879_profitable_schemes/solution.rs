// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

impl Solution {
    pub fn profitable_schemes(n: i32, min_profit: i32, group: Vec<i32>, profit: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as usize;
        let min_profit = min_profit as usize;
        let mut dp = vec![vec![0i32; min_profit + 1]; n + 1];
        dp[0][0] = 1;
        for i in 0..group.len() {
            let members = group[i] as usize;
            let p = profit[i] as usize;
            for people in (members..=n).rev() {
                for prof in (0..=min_profit).rev() {
                    let np = min_profit.min(prof + p);
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD;
                }
            }
        }
        let mut ans = 0;
        for people in 0..=n {
            ans = (ans + dp[people][min_profit]) % MOD;
        }
        ans
    }
}
