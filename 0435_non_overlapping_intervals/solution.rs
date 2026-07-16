// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by_key(|interval| interval[1]);

        let mut removed = 0;
        let mut end = i32::MIN;
        for interval in intervals {
            if interval[0] < end {
                removed += 1;
            } else {
                end = interval[1];
            }
        }
        removed
    }
}
