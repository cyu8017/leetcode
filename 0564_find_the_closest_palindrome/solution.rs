// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

impl Solution {
    fn make_palindrome(half: i64, length: usize) -> i64 {
        let text = half.to_string();
        let chars: Vec<char> = text.chars().collect();
        let mut pal = text.clone();
        if length % 2 == 0 {
            for i in (0..chars.len()).rev() {
                pal.push(chars[i]);
            }
        } else {
            for i in (0..chars.len().saturating_sub(1)).rev() {
                pal.push(chars[i]);
            }
        }
        pal.parse().unwrap_or(0)
    }

    fn pow10ll(exp: usize) -> i64 {
        let mut value = 1i64;
        for _ in 0..exp {
            value *= 10;
        }
        value
    }

    pub fn nearest_palindromic(n: String) -> String {
        let length = n.len();
        let number: i64 = n.parse().unwrap();
        let mut candidates = vec![Self::pow10ll(length - 1) - 1, Self::pow10ll(length) + 1];
        let prefix: i64 = n[..(length + 1) / 2].parse().unwrap();
        for half in prefix - 1..=prefix + 1 {
            candidates.push(Self::make_palindrome(half, length));
        }
        let mut best = -1i64;
        let mut best_diff = i64::MAX;
        for candidate in candidates {
            if candidate == number {
                continue;
            }
            let diff = (candidate - number).abs();
            if diff < best_diff || (diff == best_diff && candidate < best) {
                best = candidate;
                best_diff = diff;
            }
        }
        best.to_string()
    }
}
