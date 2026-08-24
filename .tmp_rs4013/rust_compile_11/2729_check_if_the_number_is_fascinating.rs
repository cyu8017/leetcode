struct Solution;
fn main() {}

// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

impl Solution {
    pub fn is_fascinating(n: i32) -> bool {
        let s = format!("{}{}{}", n, 2 * n, 3 * n);
        if s.len() != 9 {
            return false;
        }
        let mut cnt = [0i32; 10];
        for c in s.bytes() {
            cnt[(c - b'0') as usize] += 1;
        }
        if cnt[0] != 0 {
            return false;
        }
        (1..=9).all(|i| cnt[i] == 1)
    }
}
