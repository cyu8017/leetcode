// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

use std::collections::HashSet;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let mut x = 0i32;
        let mut y = 0i32;
        let mut seen = HashSet::new();
        seen.insert((0, 0));
        for c in path.chars() {
            match c {
                'N' => y += 1,
                'S' => y -= 1,
                'E' => x += 1,
                _ => x -= 1,
            }
            if !seen.insert((x, y)) {
                return true;
            }
        }
        false
    }
}
