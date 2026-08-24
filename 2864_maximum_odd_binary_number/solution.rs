// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let ones = s.bytes().filter(|&c| c == b'1').count();
        let zeros = s.len() - ones;
        let mut b = String::with_capacity(s.len());
        for _ in 0..ones.saturating_sub(1) {
            b.push('1');
        }
        for _ in 0..zeros {
            b.push('0');
        }
        b.push('1');
        b
    }
}
