// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

impl Solution {
    pub fn number_of_ways(s: String) -> i64 {
        let bytes = s.as_bytes();
        let mut total0 = 0i32;
        let mut total1 = 0i32;
        for &c in bytes {
            if c == b'0' {
                total0 += 1;
            } else {
                total1 += 1;
            }
        }
        let mut left0 = 0i32;
        let mut left1 = 0i32;
        let mut ans = 0i64;
        for &c in bytes {
            if c == b'0' {
                ans += left1 as i64 * (total1 - left1) as i64;
                left0 += 1;
            } else {
                ans += left0 as i64 * (total0 - left0) as i64;
                left1 += 1;
            }
        }
        ans
    }
}
