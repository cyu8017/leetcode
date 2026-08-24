// LeetCode 3945 - Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/

impl Solution {
    pub fn digit_frequency_score(mut n: i32) -> i32 {
        let mut ans = 0;
        while n > 0 {
            ans += n % 10;
            n /= 10;
        }
        ans
    }
}
