struct Solution;
// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

impl Solution {
    pub fn max_profit(prices: Vec<i32>, profits: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut ans = -1;
        for j in 0..n {
            let mut best_l = -1;
            let mut best_r = -1;
            for i in 0..j {
                if prices[i] < prices[j] && profits[i] > best_l {
                    best_l = profits[i];
                }
            }
            for k in j + 1..n {
                if prices[k] > prices[j] && profits[k] > best_r {
                    best_r = profits[k];
                }
            }
            if best_l >= 0 && best_r >= 0 {
                ans = ans.max(best_l + profits[j] + best_r);
            }
        }
        ans
    }
}

fn main() {}
