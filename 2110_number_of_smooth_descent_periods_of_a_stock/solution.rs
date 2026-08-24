// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let mut ans = 1i64;
        let mut cur = 1i64;
        for i in 1..prices.len() {
            if prices[i] == prices[i - 1] - 1 {
                cur += 1;
            } else {
                cur = 1;
            }
            ans += cur;
        }
        ans
    }
}
