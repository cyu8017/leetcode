// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

impl Solution {
    pub fn prime_palindrome(n: i32) -> i32 {
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            if x % 2 == 0 {
                return x == 2;
            }
            let mut d = 3i64;
            while d * d <= x as i64 {
                if x as i64 % d == 0 {
                    return false;
                }
                d += 2;
            }
            true
        }

        if n <= 2 {
            return 2;
        }
        if n <= 3 {
            return 3;
        }
        if n <= 5 {
            return 5;
        }
        if n <= 7 {
            return 7;
        }
        if n <= 11 {
            return 11;
        }

        for length in 1..=5 {
            let start = 10i32.pow(length - 1);
            let end = 10i32.pow(length);
            for root in start..end {
                let s = root.to_string();
                let mut pal = s.clone();
                for ch in s.chars().rev().skip(1) {
                    pal.push(ch);
                }
                if let Ok(val) = pal.parse::<i32>() {
                    if val >= n && is_prime(val) {
                        return val;
                    }
                }
            }
        }
        0
    }
}
