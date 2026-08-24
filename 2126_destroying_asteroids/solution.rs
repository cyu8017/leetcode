// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

impl Solution {
    pub fn asteroids_destroyed(mass: i32, mut asteroids: Vec<i32>) -> bool {
        asteroids.sort_unstable();
        let mut cur = mass as i64;
        for a in asteroids {
            if cur < a as i64 {
                return false;
            }
            cur += a as i64;
        }
        true
    }
}
