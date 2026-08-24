// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        let mut l = 0i32;
        let mut r = 0i32;
        let mut u = 0i32;
        for c in moves.chars() {
            match c {
                'L' => l += 1,
                'R' => r += 1,
                _ => u += 1,
            }
        }
        (l - r).abs() + u
    }
}
