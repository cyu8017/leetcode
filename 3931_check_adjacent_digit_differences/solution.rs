// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

impl Solution {
    pub fn is_adjacent_diff_at_most_two(s: String) -> bool {
        let bytes = s.as_bytes();
        for i in 1..bytes.len() {
            if (bytes[i - 1] as i32 - bytes[i] as i32).abs() > 2 {
                return false;
            }
        }
        true
    }
}
