// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

impl Solution {
    pub fn generate_the_string(n: i32) -> String {
        if n % 2 == 1 {
            "a".repeat(n as usize)
        } else {
            format!("{}b", "a".repeat((n - 1) as usize))
        }
    }
}
