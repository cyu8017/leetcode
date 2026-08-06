// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut run = 0;
        for value in arr {
            run = if value & 1 != 0 { run + 1 } else { 0 };
            if run == 3 {
                return true;
            }
        }
        false
    }
}
