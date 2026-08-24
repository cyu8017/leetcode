// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

impl Solution {
    pub fn calculate_tax(brackets: Vec<Vec<i32>>, income: i32) -> f64 {
        let mut ans = 0.0;
        let mut prev = 0;
        for b in brackets {
            let upper = b[0];
            let percent = b[1];
            if income <= prev {
                break;
            }
            let taxable = if income < upper { income - prev } else { upper - prev };
            ans += taxable as f64 * percent as f64 / 100.0;
            prev = upper;
        }
        ans
    }
}
