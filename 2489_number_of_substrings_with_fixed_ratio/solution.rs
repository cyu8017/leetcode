// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

use std::collections::HashMap;

impl Solution {
    pub fn fixed_ratio(s: String, num1: i32, num2: i32) -> i64 {
        let mut pref: HashMap<i64, i32> = HashMap::new();
        pref.insert(0, 1);
        let mut zeros = 0i64;
        let mut ones = 0i64;
        let mut ans = 0i64;
        for c in s.bytes() {
            if c == b'0' {
                zeros += 1;
            } else {
                ones += 1;
            }
            let key = zeros * num2 as i64 - ones * num1 as i64;
            ans += *pref.get(&key).unwrap_or(&0) as i64;
            *pref.entry(key).or_insert(0) += 1;
        }
        ans
    }
}
