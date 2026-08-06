// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

impl Solution {
    pub fn final_prices(prices: Vec<i32>) -> Vec<i32> {
        let mut ans = prices.clone();
        let mut stack = Vec::new();
        for (i, &price) in prices.iter().enumerate() {
            while stack.last().map(|&j| prices[j] >= price).unwrap_or(false) {
                let j = stack.pop().unwrap();
                ans[j] -= price;
            }
            stack.push(i);
        }
        ans
    }
}
