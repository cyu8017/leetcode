struct Solution;
// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

impl Solution {
    pub fn smallest_value(mut n: i32) -> i32 {
        fn sum_prime_factors(mut x: i32) -> i32 {
            let mut s = 0;
            let mut i = 2;
            while i * i <= x {
                while x % i == 0 {
                    s += i;
                    x /= i;
                }
                i += 1;
            }
            if x > 1 {
                s += x;
            }
            s
        }
        loop {
            let s = sum_prime_factors(n);
            if s == n {
                return n;
            }
            n = s;
        }
    }
}

fn main() {}
