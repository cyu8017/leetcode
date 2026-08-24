// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

impl Solution {
    pub fn at_most_n_given_digit_set(digits: Vec<String>, n: i32) -> i32 {
        let s = n.to_string();
        let m = s.len();
        let k = digits.len();
        fn ipow(base: usize, exp: usize) -> i32 {
            let mut r = 1i32;
            for _ in 0..exp {
                r *= base as i32;
            }
            r
        }
        fn count_up_to(digits: &[String], t: &str) -> i32 {
            if t.is_empty() {
                return 0;
            }
            let k = digits.len();
            let first = digits.iter().filter(|d| d.as_bytes()[0] < t.as_bytes()[0]).count() as i32;
            let mut ways = first * ipow(k, t.len() - 1);
            let found = digits.iter().any(|d| d.as_bytes()[0] == t.as_bytes()[0]);
            if found {
                ways += count_up_to(digits, &t[1..]);
            }
            ways
        }
        let mut ans = 0;
        for i in 1..m {
            ans += ipow(k, i);
        }
        ans += count_up_to(&digits, &s);
        ans
    }
}
