// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

impl Solution {
    pub fn busy_student(start_time: Vec<i32>, end_time: Vec<i32>, query_time: i32) -> i32 {
        start_time
            .into_iter()
            .zip(end_time)
            .filter(|&(s, e)| s <= query_time && query_time <= e)
            .count() as i32
    }
}
