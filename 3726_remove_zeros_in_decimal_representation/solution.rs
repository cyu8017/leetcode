// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

impl Solution {
    pub fn remove_zeros(mut n: i64) -> i64 {
        let mut ans = 0i64;
        let mut k = 1i64;
        while n > 0 {
            let x = n % 10;
            if x > 0 {
                ans = k * x + ans;
                k *= 10;
            }
            n /= 10;
        }
        ans
    }
}
