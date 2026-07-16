// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

impl Solution {
    pub fn strobogrammatic_in_range(low: String, high: String) -> i32 {
        let low_value: i64 = low.parse().unwrap_or(0);
        let high_value: i64 = high.parse().unwrap_or(0);
        let mut count = 0;

        for length in low.len()..=high.len() {
            for value in Self::build(0, length as i32 - 1) {
                let numeric: i64 = value.parse().unwrap_or(0);
                if low_value <= numeric && numeric <= high_value {
                    count += 1;
                }
            }
        }
        count
    }

    fn build(left: i32, right: i32) -> Vec<String> {
        if left > right {
            return vec![String::new()];
        }
        if left == right {
            return vec!["0".to_string(), "1".to_string(), "8".to_string()];
        }

        let pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")];
        let mut result = Vec::new();
        for (start, end) in pairs {
            if left == 0 && start == "0" {
                continue;
            }
            for middle in Self::build(left + 1, right - 1) {
                result.push(format!("{start}{middle}{end}"));
            }
        }
        result
    }
}
