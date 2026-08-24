// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let mut hold = -prices[0];
        let mut cash = 0;
        for &price in prices.iter().skip(1) {
            hold = hold.max(cash - price);
            cash = cash.max(hold + price - fee);
        }
        cash
    }
}
