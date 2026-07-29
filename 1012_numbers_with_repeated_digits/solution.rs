// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

use std::collections::HashSet;

impl Solution {
    pub fn num_dup_digits_at_most_n(n: i32) -> i32 {
        let digits: Vec<i32> = n
            .to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap() as i32)
            .collect();
        let m = digits.len();
        fn p(a: i32, b: i32) -> i32 {
            let mut res = 1;
            for i in 0..b {
                res *= a - i;
            }
            res
        }
        let mut total_unique = 0;
        for length in 1..m {
            total_unique += 9 * p(9, length as i32 - 1);
        }
        let mut used = HashSet::new();
        let mut broken = false;
        for (i, &d) in digits.iter().enumerate() {
            let start = if i == 0 { 1 } else { 0 };
            for x in start..d {
                if used.contains(&x) {
                    continue;
                }
                total_unique += p(9 - i as i32, (m - i - 1) as i32);
            }
            if used.contains(&d) {
                broken = true;
                break;
            }
            used.insert(d);
        }
        if !broken {
            total_unique += 1;
        }
        n - total_unique
    }
}
