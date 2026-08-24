struct Solution;

// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

impl Solution {
    pub fn min_max_difference(num: i32) -> i32 {
        let s: Vec<u8> = num.to_string().into_bytes();
        let remap = |from: u8, to: u8| {
            let mut v = 0i32;
            for &c in &s {
                let d = if c == from { to } else { c };
                v = v * 10 + (d - b'0') as i32;
            }
            v
        };
        let mut max_v = num;
        for &c in &s {
            if c != b'9' {
                max_v = remap(c, b'9');
                break;
            }
        }
        let min_v = remap(s[0], b'0');
        max_v - min_v
    }
}

fn main() {}
