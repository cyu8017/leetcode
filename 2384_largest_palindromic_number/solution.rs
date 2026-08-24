// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

impl Solution {
    pub fn largest_palindromic(num: String) -> String {
        let mut cnt = [0i32; 10];
        for c in num.bytes() {
            cnt[(c - b'0') as usize] += 1;
        }
        let mut left = String::new();
        for d in (0..=9).rev() {
            while cnt[d] >= 2 {
                if d == 0 && left.is_empty() {
                    break;
                }
                left.push((b'0' + d as u8) as char);
                cnt[d] -= 2;
            }
        }
        let mut mid = None;
        for d in (0..=9).rev() {
            if cnt[d] > 0 {
                mid = Some((b'0' + d as u8) as char);
                break;
            }
        }
        if left.is_empty() {
            return mid.map(|c| c.to_string()).unwrap_or_else(|| "0".to_string());
        }
        let right: String = left.chars().rev().collect();
        if let Some(m) = mid {
            format!("{}{}{}", left, m, right)
        } else {
            format!("{}{}", left, right)
        }
    }
}
