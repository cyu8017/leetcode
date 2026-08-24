struct Solution;
fn main() {}

// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

impl Solution {
    pub fn account_balance_after_purchase(purchase_amount: i32) -> i32 {
        let r = ((purchase_amount + 5) / 10) * 10;
        100 - r
    }
}
