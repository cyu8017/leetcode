// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut intervals = intervals;
        intervals.sort_by_key(|interval| interval[0]);

        let mut merged = vec![intervals[0].clone()];

        for current in intervals.into_iter().skip(1) {
            let last = merged.last_mut().unwrap();

            if current[0] <= last[1] {
                last[1] = last[1].max(current[1]);
            } else {
                merged.push(current);
            }
        }

        merged
    }
}
