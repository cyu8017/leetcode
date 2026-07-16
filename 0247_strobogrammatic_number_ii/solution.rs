// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

impl Solution {
    pub fn find_strobogrammatic(n: i32) -> Vec<String> {
        Self::build(0, n - 1)
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
