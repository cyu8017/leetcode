// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        let mut available: BinaryHeap<Reverse<(i32, usize)>> = servers
            .iter()
            .enumerate()
            .map(|(index, &weight)| Reverse((weight, index)))
            .collect();
        let mut busy: BinaryHeap<Reverse<(i64, i32, usize)>> = BinaryHeap::new();
        let mut answer = Vec::with_capacity(tasks.len());
        let mut time: i64 = 0;

        for (moment, &task) in tasks.iter().enumerate() {
            time = time.max(moment as i64);
            while let Some(Reverse((finish, weight, index))) = busy.peek().copied() {
                if finish <= time {
                    busy.pop();
                    available.push(Reverse((weight, index)));
                } else {
                    break;
                }
            }
            while available.is_empty() {
                if let Some(Reverse((finish, _, _))) = busy.peek().copied() {
                    time = finish;
                }
                while let Some(Reverse((finish, weight, index))) = busy.peek().copied() {
                    if finish <= time {
                        busy.pop();
                        available.push(Reverse((weight, index)));
                    } else {
                        break;
                    }
                }
            }
            let Reverse((weight, index)) = available.pop().unwrap();
            busy.push(Reverse((time + task as i64, weight, index)));
            answer.push(index as i32);
        }
        answer
    }
}
