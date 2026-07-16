// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, mut new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut i = 0;

        while i < intervals.len() && intervals[i][1] < new_interval[0] {
            result.push(intervals[i].clone());
            i += 1;
        }

        while i < intervals.len() && intervals[i][0] <= new_interval[1] {
            new_interval[0] = new_interval[0].min(intervals[i][0]);
            new_interval[1] = new_interval[1].max(intervals[i][1]);
            i += 1;
        }

        result.push(new_interval);

        while i < intervals.len() {
            result.push(intervals[i].clone());
            i += 1;
        }

        result
    }
}
