// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

impl Solution {
    pub fn possible_string_count(word: String) -> i32 {
        let w = word.as_bytes();
        let mut ans = 1;
        for i in 1..w.len() {
            if w[i] == w[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}
