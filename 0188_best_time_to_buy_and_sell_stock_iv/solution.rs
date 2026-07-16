// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
        let k = k as usize;
        if prices.is_empty() || k == 0 {
            return 0;
        }
        if k >= prices.len() / 2 {
            return prices.windows(2).map(|days| (days[1] - days[0]).max(0)).sum();
        }

        let mut buy = vec![i32::MAX; k + 1];
        let mut sell = vec![0; k + 1];
        for price in prices {
            for transaction in 1..=k {
                buy[transaction] = buy[transaction].min(price - sell[transaction - 1]);
                sell[transaction] = sell[transaction].max(price - buy[transaction]);
            }
        }
        sell[k]
    }
}