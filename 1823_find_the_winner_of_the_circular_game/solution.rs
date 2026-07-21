// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

impl Solution {
    pub fn find_the_winner(n: i32, k: i32) -> i32 {
        let mut pos = 0;
        for size in 2..=n {
            pos = (pos + k) % size;
        }
        pos + 1
    }
}
