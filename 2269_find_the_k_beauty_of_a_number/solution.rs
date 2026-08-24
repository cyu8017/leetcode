// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

impl Solution {
    pub fn divisor_substrings(num: i32, k: i32) -> i32 {
        let s = num.to_string();
        let bytes = s.as_bytes();
        let k = k as usize;
        let mut ans = 0;
        for i in 0..=bytes.len().saturating_sub(k) {
            let mut sub = 0i32;
            for j in 0..k {
                sub = sub * 10 + (bytes[i + j] - b'0') as i32;
            }
            if sub != 0 && num % sub == 0 {
                ans += 1;
            }
        }
        ans
    }
}
