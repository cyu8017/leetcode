// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        if time_series.is_empty() {
            return 0;
        }
        let mut total = duration;
        for index in 1..time_series.len() {
            total += duration.min(time_series[index] - time_series[index - 1]);
        }
        total
    }
}
