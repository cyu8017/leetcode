// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

impl Solution {
    pub fn max_tastiness(
        price: Vec<i32>,
        tastiness: Vec<i32>,
        max_amount: i32,
        max_coupons: i32,
    ) -> i32 {
        let n = price.len();
        let max_amount = max_amount as usize;
        let max_coupons = max_coupons as usize;
        let mut dp = vec![vec![i32::MIN / 2; max_coupons + 1]; max_amount + 1];
        dp[0][0] = 0;
        for i in 0..n {
            let p = price[i] as usize;
            let t = tastiness[i];
            for a in (0..=max_amount).rev() {
                for c in (0..=max_coupons).rev() {
                    if dp[a][c] < 0 {
                        continue;
                    }
                    if a + p <= max_amount {
                        dp[a + p][c] = dp[a + p][c].max(dp[a][c] + t);
                    }
                    if c + 1 <= max_coupons && a + p / 2 <= max_amount {
                        dp[a + p / 2][c + 1] = dp[a + p / 2][c + 1].max(dp[a][c] + t);
                    }
                }
            }
        }
        let mut ans = 0;
        for a in 0..=max_amount {
            for c in 0..=max_coupons {
                ans = ans.max(dp[a][c]);
            }
        }
        ans
    }
}
