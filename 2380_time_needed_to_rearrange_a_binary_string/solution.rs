// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

impl Solution {
    pub fn seconds_to_remove_occurrences(s: String) -> i32 {
        let mut ans = 0;
        let mut zeros = 0;
        for c in s.chars() {
            if c == '0' {
                zeros += 1;
            } else if zeros > 0 {
                ans = (ans + 1).max(zeros);
            }
        }
        ans
    }
}
