// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

use std::sync::Mutex;

struct DiningPhilosophers {
    forks: [Mutex<()>; 5],
}

impl DiningPhilosophers {
    pub fn new() -> Self {
        Self {
            forks: [
                Mutex::new(()),
                Mutex::new(()),
                Mutex::new(()),
                Mutex::new(()),
                Mutex::new(()),
            ],
        }
    }

    pub fn wants_to_eat(
        &self,
        philosopher: i32,
        pick_left_fork: impl FnOnce(),
        pick_right_fork: impl FnOnce(),
        eat: impl FnOnce(),
        put_left_fork: impl FnOnce(),
        put_right_fork: impl FnOnce(),
    ) {
        let left = philosopher as usize;
        let right = (philosopher as usize + 1) % 5;
        let (first, second) = if philosopher % 2 != 0 {
            (right, left)
        } else {
            (left, right)
        };
        let _f1 = self.forks[first].lock().unwrap();
        let _f2 = self.forks[second].lock().unwrap();
        pick_left_fork();
        pick_right_fork();
        eat();
        put_left_fork();
        put_right_fork();
    }
}
