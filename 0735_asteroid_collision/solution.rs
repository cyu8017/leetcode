// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::new();
        for asteroid in asteroids {
            let mut alive = true;
            while alive && !stack.is_empty() && asteroid < 0 && *stack.last().unwrap() > 0 {
                let top = *stack.last().unwrap();
                if top < -asteroid {
                    stack.pop();
                    continue;
                }
                if top == -asteroid {
                    stack.pop();
                }
                alive = false;
            }
            if alive {
                stack.push(asteroid);
            }
        }
        stack
    }
}
