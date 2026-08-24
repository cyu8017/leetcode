struct Solution;
// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

impl Solution {
    pub fn filter_occupied_intervals(
        mut occupied_intervals: Vec<Vec<i32>>,
        free_start: i32,
        free_end: i32,
    ) -> Vec<Vec<i32>> {
        occupied_intervals.sort_by_key(|a| a[0]);
        let mut busy = vec![occupied_intervals[0].clone()];
        for cur in occupied_intervals.into_iter().skip(1) {
            let last = busy.last_mut().unwrap();
            if last[1] + 1 < cur[0] {
                busy.push(cur);
            } else if cur[1] > last[1] {
                last[1] = cur[1];
            }
        }
        let mut ans = Vec::new();
        for it in busy {
            let s = it[0];
            let e = it[1];
            if e < free_start || s > free_end {
                ans.push(vec![s, e]);
            } else {
                if s < free_start {
                    ans.push(vec![s, free_start - 1]);
                }
                if e > free_end {
                    ans.push(vec![free_end + 1, e]);
                }
            }
        }
        ans
    }
}

fn main() {}
