// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

impl Solution { pub fn max_profit(prices: Vec<i32>) -> i32 { let mut low=i32::MAX;let mut best=0;for price in prices{low=low.min(price);best=best.max(price-low);}best } }