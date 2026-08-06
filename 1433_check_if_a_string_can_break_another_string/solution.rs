// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

impl Solution {
    pub fn check_if_can_break(s1: String, s2: String) -> bool {
        let mut a: Vec<char> = s1.chars().collect();
        let mut b: Vec<char> = s2.chars().collect();
        a.sort_unstable();
        b.sort_unstable();
        a.iter().zip(b.iter()).all(|(x, y)| x >= y) || a.iter().zip(b.iter()).all(|(x, y)| x <= y)
    }
}
