// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

impl Solution {
    pub fn add_operators(num: String, target: i32) -> Vec<String> {
        let digits = num.as_bytes();
        let mut result = Vec::new();

        fn backtrack(
            digits: &[u8],
            target: i32,
            index: usize,
            path: String,
            value: i64,
            previous: i64,
            result: &mut Vec<String>,
        ) {
            if index == digits.len() {
                if value == target as i64 {
                    result.push(path);
                }
                return;
            }

            for end in index..digits.len() {
                if end > index && digits[index] == b'0' {
                    break;
                }
                let current_str = std::str::from_utf8(&digits[index..=end]).unwrap();
                let current = current_str.parse::<i64>().unwrap();
                if index == 0 {
                    backtrack(digits, target, end + 1, current_str.to_string(), current, current, result);
                } else {
                    backtrack(
                        digits,
                        target,
                        end + 1,
                        format!("{path}+{current_str}"),
                        value + current,
                        current,
                        result,
                    );
                    backtrack(
                        digits,
                        target,
                        end + 1,
                        format!("{path}-{current_str}"),
                        value - current,
                        -current,
                        result,
                    );
                    backtrack(
                        digits,
                        target,
                        end + 1,
                        format!("{path}*{current_str}"),
                        value - previous + previous * current,
                        previous * current,
                        result,
                    );
                }
            }
        }

        backtrack(digits, target, 0, String::new(), 0, 0, &mut result);
        result
    }
}
