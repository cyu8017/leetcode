struct Solution;
// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

impl Solution {
    pub fn max_distance(moves: String) -> i32 {
        let mut x: i32 = 0;
        let mut y: i32 = 0;
        let mut z: i32 = 0;
        for c in moves.chars() {
            match c {
                'U' => x -= 1,
                'D' => x += 1,
                'L' => y -= 1,
                'R' => y += 1,
                _ => z += 1,
            }
        }
        x.abs() + y.abs() + z
    }
}

fn main() {}
