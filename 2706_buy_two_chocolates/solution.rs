// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

impl Solution {
    pub fn buy_choco(mut prices: Vec<i32>, money: i32) -> i32 {
        prices.sort_unstable();
        let cost = prices[0] + prices[1];
        if cost <= money {
            money - cost
        } else {
            money
        }
    }
}
