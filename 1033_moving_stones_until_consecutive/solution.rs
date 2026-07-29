// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

impl Solution {
    pub fn num_moves_stones(a: i32, b: i32, c: i32) -> Vec<i32> {
        let mut v = [a, b, c];
        v.sort_unstable();
        let (x, y, z) = (v[0], v[1], v[2]);
        let min_moves = if z - x == 2 {
            0
        } else if y - x <= 2 || z - y <= 2 {
            1
        } else {
            2
        };
        vec![min_moves, z - x - 2]
    }
}
