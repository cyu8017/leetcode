// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

use std::collections::HashSet;

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let s: HashSet<&str> = nums.iter().map(|x| x.as_str()).collect();
        let n = nums.len();
        let preferred = [
            "11", "101", "00", "10", "01", "000", "001", "010", "011", "100", "110", "111",
        ];
        for cand in preferred {
            if cand.len() == n && !s.contains(cand) {
                return cand.to_string();
            }
        }
        for i in 0..(1 << n) {
            let cand = format!("{:0width$b}", i, width = n);
            if !s.contains(cand.as_str()) {
                return cand;
            }
        }
        "0".repeat(n)
    }
}
