// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        let mut answer = vec![0u8; s.len()];
        for (i, ch) in s.bytes().enumerate() {
            answer[indices[i] as usize] = ch;
        }
        String::from_utf8(answer).unwrap()
    }
}
