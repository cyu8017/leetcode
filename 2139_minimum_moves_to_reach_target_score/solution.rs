// LeetCode 2139 - Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/

impl Solution {
    pub fn min_moves(mut target: i32, mut max_doubles: i32) -> i32 {
        let mut ans = 0;
        while target > 1 && max_doubles > 0 {
            if target % 2 == 1 {
                target -= 1;
                ans += 1;
            } else {
                target /= 2;
                max_doubles -= 1;
                ans += 1;
            }
        }
        ans + target - 1
    }
}
