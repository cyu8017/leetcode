// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }

        let n1 = num1.as_bytes();
        let n2 = num2.as_bytes();
        let mut positions = vec![0i32; n1.len() + n2.len()];

        for i in (0..n1.len()).rev() {
            for j in (0..n2.len()).rev() {
                let product = (n1[i] - b'0') as i32 * (n2[j] - b'0') as i32;
                let low = i + j + 1;
                let high = i + j;
                let total = product + positions[low];
                positions[low] = total % 10;
                positions[high] += total / 10;
            }
        }

        let result: String = positions
            .iter()
            .map(|&digit| (b'0' + digit as u8) as char)
            .collect();

        let trimmed = result.trim_start_matches('0');
        if trimmed.is_empty() {
            "0".to_string()
        } else {
            trimmed.to_string()
        }
    }
}
