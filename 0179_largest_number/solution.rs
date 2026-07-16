// LeetCode 0179 - Largest Number
// https://leetcode.com/problems/largest-number/

impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut parts: Vec<String> = nums.into_iter().map(|num| num.to_string()).collect();
        parts.sort_by(|a, b| (b.clone() + a).cmp(&(a.clone() + b)));
        if parts[0] == "0" {
            return "0".to_string();
        }
        parts.concat()
    }
}