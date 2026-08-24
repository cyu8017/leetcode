// LeetCode 3871 - Count Commas in Range II
// https://leetcode.com/problems/count-commas-in-range-ii/

impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut ans = 0i64;
        let mut x = 1000i64;
        while x <= n {
            ans += n - x + 1;
            if x > i64::MAX / 1000 {
                break;
            }
            x *= 1000;
        }
        ans
    }
}
