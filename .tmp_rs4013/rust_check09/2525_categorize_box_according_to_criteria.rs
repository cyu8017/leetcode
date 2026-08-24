struct Solution;

// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

impl Solution {
    pub fn categorize_box(length: i32, width: i32, height: i32, mass: i32) -> String {
        let bulky = length >= 10000
            || width >= 10000
            || height >= 10000
            || (length as i64) * (width as i64) * (height as i64) >= 1_000_000_000;
        let heavy = mass >= 100;
        if bulky && heavy {
            "Both".to_string()
        } else if bulky {
            "Bulky".to_string()
        } else if heavy {
            "Heavy".to_string()
        } else {
            "Neither".to_string()
        }
    }
}

fn main() {}
