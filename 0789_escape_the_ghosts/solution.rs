// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

impl Solution {
    pub fn escape_ghosts(ghosts: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let target_dist = target[0].abs() + target[1].abs();
        for ghost in &ghosts {
            if (ghost[0] - target[0]).abs() + (ghost[1] - target[1]).abs() <= target_dist {
                return false;
            }
        }
        true
    }
}
