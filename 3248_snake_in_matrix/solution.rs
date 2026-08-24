// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

impl Solution {
    pub fn final_position_of_snake(n: i32, commands: Vec<String>) -> i32 {
        let mut x = 0;
        let mut y = 0;
        for c in commands {
            match c.as_bytes()[0] {
                b'U' => x -= 1,
                b'D' => x += 1,
                b'L' => y -= 1,
                b'R' => y += 1,
                _ => {}
            }
        }
        x * n + y
    }
}
