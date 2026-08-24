struct Solution;
// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

use std::collections::BinaryHeap;

impl Solution {
    pub fn schedule_course(mut courses: Vec<Vec<i32>>) -> i32 {
        courses.sort_by_key(|c| c[1]);
        let mut heap = BinaryHeap::new();
        let mut time = 0;
        for course in courses {
            let duration = course[0];
            let last_day = course[1];
            if time + duration <= last_day {
                heap.push(duration);
                time += duration;
            } else if let Some(&top) = heap.peek() {
                if top > duration {
                    time += duration - top;
                    heap.pop();
                    heap.push(duration);
                }
            }
        }
        heap.len() as i32
    }
}

fn main() {}
