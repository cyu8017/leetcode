// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let bytes = s.as_bytes();
        if bytes.is_empty() || bytes[0] == b'0' {
            return 0;
        }

        let mut prev2 = 1;
        let mut prev1 = 1;

        for i in 1..bytes.len() {
            let mut current = 0;
            if bytes[i] != b'0' {
                current += prev1;
            }
            let two = (bytes[i - 1] - b'0') as i32 * 10 + (bytes[i] - b'0') as i32;
            if (10..=26).contains(&two) {
                current += prev2;
            }
            prev2 = prev1;
            prev1 = current;
        }

        prev1
    }
}
