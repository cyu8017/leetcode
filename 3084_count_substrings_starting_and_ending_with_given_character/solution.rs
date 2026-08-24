// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

impl Solution {
    pub fn count_substrings(s: String, c: char) -> i64 {
        let cnt = s.chars().filter(|&ch| ch == c).count() as i64;
        cnt + cnt * (cnt - 1) / 2
    }
}
