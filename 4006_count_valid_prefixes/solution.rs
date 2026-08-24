// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

impl Solution {
    pub fn count_valid_prefixes(s: String) -> i32 {
        let mut ans = 0;
        let mut t = 0;
        for c in s.chars() {
            if c == '1' {
                t += 1;
            } else {
                t -= 1;
            }
            if (-1..=1).contains(&t) {
                ans += 1;
            }
        }
        ans
    }
}
