// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

impl Solution { pub fn max_profit(prices: Vec<i32>) -> i32 { let(mut b1,mut b2,mut s1,mut s2)=(i32::MAX,i32::MAX,0,0);for price in prices{b1=b1.min(price);s1=s1.max(price-b1);b2=b2.min(price-s1);s2=s2.max(price-b2);}s2 } }