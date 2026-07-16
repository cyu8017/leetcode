// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

use std::collections::HashSet;

pub trait Robot {
    fn r#move(&mut self) -> bool;
    fn turn_left(&mut self);
    fn turn_right(&mut self);
    fn clean(&mut self);
}

impl Solution {
    fn backtrack(
        robot: &mut dyn Robot,
        row: i32,
        col: i32,
        direction: i32,
        visited: &mut HashSet<(i32, i32, i32)>,
    ) {
        robot.clean();
        let directions = [(-1, 0), (0, 1), (1, 0), (0, -1)];
        for step in 0..4 {
            let next_direction = (direction + step) % 4;
            let (dr, dc) = directions[next_direction as usize];
            let next_row = row + dr;
            let next_col = col + dc;
            if !visited.contains(&(next_row, next_col, next_direction)) && robot.r#move() {
                visited.insert((next_row, next_col, next_direction));
                Self::backtrack(robot, next_row, next_col, next_direction, visited);
                robot.turn_right();
                robot.turn_right();
                robot.r#move();
                robot.turn_right();
                robot.turn_right();
            }
            robot.turn_right();
        }
    }

    pub fn clean_room(robot: &mut dyn Robot) {
        let mut visited = HashSet::new();
        visited.insert((0, 0, 0));
        Self::backtrack(robot, 0, 0, 0, &mut visited);
    }
}
