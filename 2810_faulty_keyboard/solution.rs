// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

impl Solution {
    pub fn final_string(s: String) -> String {
        let mut b = Vec::new();
        for c in s.chars() {
            if c == 'i' {
                b.reverse();
            } else {
                b.push(c);
            }
        }
        b.into_iter().collect()
    }
}
