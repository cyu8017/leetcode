// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

impl Solution {
    pub fn consecutive_numbers_sum(n: i32) -> i32 {
        let n = n as i64;
        let mut ans = 0;
        let mut k = 1i64;
        while k * (k - 1) / 2 < n {
            if (n - k * (k - 1) / 2) % k == 0 {
                ans += 1;
            }
            k += 1;
        }
        ans
    }
}
