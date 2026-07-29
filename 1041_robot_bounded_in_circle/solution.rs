// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

impl Solution {
    pub fn is_robot_bounded(instructions: String) -> bool {
        let mut x = 0;
        let mut y = 0;
        let mut dx = 0;
        let mut dy = 1;
        for ch in instructions.chars() {
            match ch {
                'G' => {
                    x += dx;
                    y += dy;
                }
                'L' => {
                    let (ndx, ndy) = (-dy, dx);
                    dx = ndx;
                    dy = ndy;
                }
                _ => {
                    let (ndx, ndy) = (dy, -dx);
                    dx = ndx;
                    dy = ndy;
                }
            }
        }
        (x == 0 && y == 0) || !(dx == 0 && dy == 1)
    }
}
