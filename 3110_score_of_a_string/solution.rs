// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 0;
        for i in 1..b.len() {
            ans += (b[i - 1] as i32 - b[i] as i32).abs();
        }
        ans
    }
}
