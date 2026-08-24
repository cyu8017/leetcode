// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let bytes = answer_key.as_bytes();
        let max_with = |ch: u8| -> i32 {
            let mut left = 0;
            let mut bad = 0;
            let mut best = 0;
            for right in 0..bytes.len() {
                if bytes[right] != ch {
                    bad += 1;
                }
                while bad > k {
                    if bytes[left] != ch {
                        bad -= 1;
                    }
                    left += 1;
                }
                best = best.max((right - left + 1) as i32);
            }
            best
        };
        max_with(b'T').max(max_with(b'F'))
    }
}
