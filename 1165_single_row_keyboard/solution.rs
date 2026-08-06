// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

impl Solution {
    pub fn calculate_time(keyboard: String, word: String) -> i32 {
        let mut pos = [0; 26];
        for (i, b) in keyboard.bytes().enumerate() {
            pos[(b - b'a') as usize] = i as i32;
        }
        let mut ans = 0;
        let mut cur = 0;
        for b in word.bytes() {
            let next = pos[(b - b'a') as usize];
            ans += (next - cur).abs();
            cur = next;
        }
        ans
    }
}
