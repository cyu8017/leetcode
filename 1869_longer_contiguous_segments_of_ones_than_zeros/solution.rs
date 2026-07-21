// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

impl Solution {
    pub fn check_zero_ones(s: String) -> bool {
        let mut max_zeros = 0i32;
        let mut max_ones = 0i32;
        let mut zeros = 0i32;
        let mut ones = 0i32;
        for ch in s.bytes() {
            if ch == b'0' {
                zeros += 1;
                ones = 0;
                max_zeros = max_zeros.max(zeros);
            } else {
                ones += 1;
                zeros = 0;
                max_ones = max_ones.max(ones);
            }
        }
        max_ones > max_zeros
    }
}
