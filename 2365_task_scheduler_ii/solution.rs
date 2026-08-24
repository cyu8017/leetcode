// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

use std::collections::HashMap;

impl Solution {
    pub fn task_scheduler_ii(tasks: Vec<i32>, space: i32) -> i64 {
        let mut next = HashMap::new();
        let mut day = 0i64;
        for t in tasks {
            if let Some(&nd) = next.get(&t) {
                if nd > day {
                    day = nd;
                }
            }
            day += 1;
            next.insert(t, day + space as i64);
        }
        day
    }
}
