// LeetCode 0402 - Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

impl Solution {
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let mut stack: Vec<u8> = Vec::new();
        let mut remaining = k;

        for digit in num.bytes() {
            while remaining > 0 && !stack.is_empty() && *stack.last().unwrap() > digit {
                stack.pop();
                remaining -= 1;
            }
            stack.push(digit);
        }

        if remaining > 0 {
            let keep = stack.len() - remaining as usize;
            stack.truncate(keep);
        }

        let mut start = 0;
        while start + 1 < stack.len() && stack[start] == b'0' {
            start += 1;
        }

        let result = String::from_utf8(stack[start..].to_vec()).unwrap_or_else(|_| "0".to_string());
        if result.is_empty() {
            "0".to_string()
        } else {
            result
        }
    }
}
