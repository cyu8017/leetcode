// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut ans = 0;
        for c in s.bytes() {
            if c != b'a' {
                ans = ans.max(26 - (c - b'a') as i32);
            }
        }
        ans
    }
}
