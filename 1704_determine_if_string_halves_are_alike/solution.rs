// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let mid = s.len() / 2;
        let mut balance = 0i32;
        for (i, ch) in s.chars().enumerate() {
            if "aeiouAEIOU".contains(ch) {
                balance += if i < mid { 1 } else { -1 };
            }
        }
        balance == 0
    }
}
