// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

impl Solution {
    pub fn number_of_lines(widths: Vec<i32>, s: String) -> Vec<i32> {
        let mut lines = 1;
        let mut width = 0;
        for ch in s.bytes() {
            let w = widths[(ch - b'a') as usize];
            if width + w > 100 {
                lines += 1;
                width = w;
            } else {
                width += w;
            }
        }
        vec![lines, width]
    }
}
