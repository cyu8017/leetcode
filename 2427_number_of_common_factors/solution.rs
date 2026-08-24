// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

impl Solution {
    pub fn common_factors(a: i32, b: i32) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let g = gcd(a, b);
        let mut ans = 0;
        let mut i = 1;
        while i * i <= g {
            if g % i == 0 {
                ans += 1;
                if i * i != g {
                    ans += 1;
                }
            }
            i += 1;
        }
        ans
    }
}
