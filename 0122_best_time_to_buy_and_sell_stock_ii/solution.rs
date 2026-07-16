// LeetCode 0122 - Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

impl Solution { pub fn max_profit(prices: Vec<i32>) -> i32 { prices.windows(2).map(|pair|(pair[1]-pair[0]).max(0)).sum() } }