// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

impl Solution {
    pub fn partition_string(s: String) -> i32 {
        let mut ans = 1;
        let mut seen = 0i32;
        for c in s.bytes() {
            let bit = 1 << (c - b'a');
            if seen & bit != 0 {
                ans += 1;
                seen = 0;
            }
            seen |= bit;
        }
        ans
    }
}
