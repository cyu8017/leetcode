// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

impl Solution {
    pub fn minimum_relative_losses(mut prices: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        prices.sort_unstable();
        let n = prices.len();
        let mut ans = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let k = q[0];
            let m = q[1] as usize;
            let mut losses = vec![0i64; n];
            for i in 0..n {
                if prices[i] <= k {
                    losses[i] = prices[i] as i64;
                } else {
                    losses[i] = 2 * k as i64 - prices[i] as i64;
                }
            }
            losses.sort_unstable();
            ans[qi] = losses.iter().take(m).sum();
        }
        ans
    }
}
