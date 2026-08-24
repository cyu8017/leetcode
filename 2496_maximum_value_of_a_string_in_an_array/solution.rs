// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

impl Solution {
    pub fn maximum_value(strs: Vec<String>) -> i32 {
        let mut ans = 0;
        for s in strs {
            let mut all_digit = true;
            let mut val = 0;
            for c in s.bytes() {
                if c < b'0' || c > b'9' {
                    all_digit = false;
                    break;
                }
                val = val * 10 + (c - b'0') as i32;
            }
            if !all_digit {
                val = s.len() as i32;
            }
            if val > ans {
                ans = val;
            }
        }
        ans
    }
}
