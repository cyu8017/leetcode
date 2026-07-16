// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.is_empty() {
            return 0;
        }
        let mut free = 0;
        let mut hold = -prices[0];
        let mut cooldown = 0;
        for &price in prices.iter().skip(1) {
            let next_free = free.max(cooldown);
            let next_hold = hold.max(free - price);
            let next_cooldown = hold + price;
            free = next_free;
            hold = next_hold;
            cooldown = next_cooldown;
        }
        free.max(cooldown)
    }
}
