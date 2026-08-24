// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

impl Solution {
    pub fn minimum_chairs(s: String) -> i32 {
        let mut cnt = 0;
        let mut left = 0;
        for c in s.chars() {
            if c == 'E' {
                if left > 0 {
                    left -= 1;
                } else {
                    cnt += 1;
                }
            } else {
                left += 1;
            }
        }
        cnt
    }
}
