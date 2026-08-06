// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

impl Solution {
    pub fn max_score(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut ones = bytes.iter().filter(|&&c| c == b'1').count() as i32;
        let mut left_zeros = 0;
        let mut answer = 0;
        for &ch in &bytes[..bytes.len() - 1] {
            if ch == b'0' {
                left_zeros += 1;
            } else {
                ones -= 1;
            }
            answer = answer.max(left_zeros + ones);
        }
        answer
    }
}
