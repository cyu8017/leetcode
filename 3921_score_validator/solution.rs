// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

impl Solution {
    pub fn score_validator(events: Vec<String>) -> Vec<i32> {
        let mut score = 0;
        let mut counter = 0;
        for event in events {
            let bytes = event.as_bytes();
            let mut is_num = !bytes.is_empty();
            let mut num = 0i32;
            let mut start = 0usize;
            if is_num && bytes[0] == b'-' {
                start = 1;
            }
            for i in start..bytes.len() {
                if bytes[i] < b'0' || bytes[i] > b'9' {
                    is_num = false;
                    break;
                }
                num = num * 10 + (bytes[i] - b'0') as i32;
            }
            if is_num && !(start == 1 && bytes.len() == 1) {
                if start == 1 {
                    num = -num;
                }
                score += num;
            } else if event == "W" {
                counter += 1;
                if counter == 10 {
                    break;
                }
            } else {
                score += 1;
            }
        }
        vec![score, counter]
    }
}
