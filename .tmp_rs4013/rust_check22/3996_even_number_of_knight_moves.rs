struct Solution;
// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

impl Solution {
    pub fn can_reach(start: Vec<i32>, target: Vec<i32>) -> bool {
        (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2
    }
}

fn main() {}
