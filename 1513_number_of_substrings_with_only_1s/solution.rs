// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let mut ans = 0i64;
        let mut run = 0i64;
        for ch in s.bytes() {
            if ch == b'1' {
                run += 1;
                ans += run;
            } else {
                run = 0;
            }
        }
        (ans % 1_000_000_007) as i32
    }
}
