// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

impl Solution {
    pub fn minimum_lines(mut stock_prices: Vec<Vec<i32>>) -> i32 {
        if stock_prices.len() <= 1 {
            return 0;
        }
        stock_prices.sort_unstable();
        let mut ans = 1;
        for i in 2..stock_prices.len() {
            let x0 = stock_prices[i - 2][0] as i64;
            let y0 = stock_prices[i - 2][1] as i64;
            let x1 = stock_prices[i - 1][0] as i64;
            let y1 = stock_prices[i - 1][1] as i64;
            let x2 = stock_prices[i][0] as i64;
            let y2 = stock_prices[i][1] as i64;
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0) {
                ans += 1;
            }
        }
        ans
    }
}
