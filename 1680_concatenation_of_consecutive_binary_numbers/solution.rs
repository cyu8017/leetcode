// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        let mut ans: i64 = 0;
        let mut bits = 0i64;
        let m = 1_000_000_007i64;
        for x in 1..=n as i64 {
            if x & (x - 1) == 0 {
                bits += 1;
            }
            ans = ((ans << bits) + x) % m;
        }
        ans as i32
    }
}
