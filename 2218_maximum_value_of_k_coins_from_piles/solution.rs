// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

impl Solution {
    pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0; k + 1];
        for pile in piles {
            let mut ndp = dp.clone();
            let mut sum = 0;
            for take in 1..=pile.len().min(k) {
                sum += pile[take - 1];
                for j in take..=k {
                    ndp[j] = ndp[j].max(dp[j - take] + sum);
                }
            }
            dp = ndp;
        }
        dp[k]
    }
}
