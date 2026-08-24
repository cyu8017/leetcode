// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

impl Solution {
    pub fn digit_sum(mut s: String, k: i32) -> String {
        let k = k as usize;
        while s.len() > k {
            let bytes = s.as_bytes();
            let mut next = String::new();
            let mut i = 0;
            while i < bytes.len() {
                let end = (i + k).min(bytes.len());
                let mut sum = 0;
                for j in i..end {
                    sum += (bytes[j] - b'0') as i32;
                }
                next.push_str(&sum.to_string());
                i += k;
            }
            s = next;
        }
        s
    }
}
