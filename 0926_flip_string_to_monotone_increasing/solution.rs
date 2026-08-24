// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let mut ones = 0;
        let mut ans = 0;
        for ch in s.bytes() {
            if ch == b'1' {
                ones += 1;
            } else {
                ans = (ans + 1).min(ones);
            }
        }
        ans
    }
}
