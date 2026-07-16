// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

impl Solution {
    pub fn restore_ip_addresses(s: String) -> Vec<String> {
        let bytes = s.as_bytes();
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn to_int(part: &[u8]) -> i32 {
            let mut value = 0;
            for &b in part {
                value = value * 10 + (b - b'0') as i32;
            }
            value
        }

        fn backtrack(
            bytes: &[u8],
            start: usize,
            path: &mut Vec<String>,
            result: &mut Vec<String>,
        ) {
            if path.len() == 4 {
                if start == bytes.len() {
                    result.push(path.join("."));
                }
                return;
            }

            for length in 1..=3 {
                if start + length > bytes.len() {
                    break;
                }
                let part = &bytes[start..start + length];
                if (part[0] == b'0' && part.len() > 1) || to_int(part) > 255 {
                    continue;
                }
                path.push(String::from_utf8(part.to_vec()).unwrap());
                backtrack(bytes, start + length, path, result);
                path.pop();
            }
        }

        backtrack(bytes, 0, &mut path, &mut result);
        result
    }
}
