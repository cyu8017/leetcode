// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let mut s = 0;
        let mut p = 1;
        let mut x = n;
        while x != 0 {
            let v = x % 10;
            x /= 10;
            s += v;
            p *= v;
        }
        n % (s + p) == 0
    }
}
