// LeetCode 1359 - Count All Valid Pickup and Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

impl Solution {
    pub fn count_orders(n: i32) -> i32 {
        let mut ans: i64 = 1;
        const MOD: i64 = 1_000_000_007;
        for i in 1..=n as i64 {
            ans = ans * i * (2 * i - 1) % MOD;
        }
        ans as i32
    }
}
