// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

impl Solution {
    pub fn is_additive_number(num: String) -> bool {
        fn valid(num: &str, mut first: String, mut second: String, mut start: usize) -> bool {
            if (first.len() > 1 && first.starts_with('0')) || (second.len() > 1 && second.starts_with('0')) {
                return false;
            }
            while start < num.len() {
                let total = (first.parse::<i64>().unwrap_or(0) + second.parse::<i64>().unwrap_or(0)).to_string();
                if !num[start..].starts_with(&total) {
                    return false;
                }
                first = second;
                second = total.clone();
                start += total.len();
            }
            true
        }

        let bytes = num.as_bytes();
        for first_end in 1..bytes.len() {
            for second_end in first_end + 1..bytes.len() {
                if valid(
                    &num,
                    num[..first_end].to_string(),
                    num[first_end..second_end].to_string(),
                    second_end,
                ) {
                    return true;
                }
            }
        }
        false
    }
}
