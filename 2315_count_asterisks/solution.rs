// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

impl Solution {
    pub fn count_asterisks(s: String) -> i32 {
        let mut ans = 0;
        let mut inside = false;
        for c in s.chars() {
            if c == '|' {
                inside = !inside;
            } else if c == '*' && !inside {
                ans += 1;
            }
        }
        ans
    }
}
