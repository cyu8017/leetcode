// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

impl Solution {
    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>, k: i32) -> i64 {
        let n = prices.len();
        let k = k as usize;
        let mut s = vec![0i64; n + 1];
        let mut t = vec![0i64; n + 1];
        for i in 1..=n {
            s[i] = s[i - 1] + prices[i - 1] as i64 * strategy[i - 1] as i64;
            t[i] = t[i - 1] + prices[i - 1] as i64;
        }
        let mut ans = s[n];
        for i in k..=n {
            ans = ans.max(s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]));
        }
        ans
    }
}
