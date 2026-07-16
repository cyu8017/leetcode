// LeetCode 0390 - Elimination Game
// https://leetcode.com/problems/elimination-game/

impl Solution {
    pub fn last_remaining(n: i32) -> i32 {
        let mut left = 1;
        let mut right = n;
        let mut step = 1;
        let mut remaining = n;
        let mut from_left = true;

        while left < right {
            if from_left || remaining % 2 == 1 {
                left += step;
            }
            right -= step;
            step *= 2;
            remaining /= 2;
            from_left = !from_left;
        }

        left
    }
}
