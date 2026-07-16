// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

impl Solution {
    pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        let mut indexed: Vec<(i32, i32)> = intervals
            .iter()
            .enumerate()
            .map(|(index, interval)| (interval[0], index as i32))
            .collect();
        indexed.sort_unstable_by_key(|entry| entry.0);

        let starts: Vec<i32> = indexed.iter().map(|entry| entry.0).collect();
        let mut result = Vec::with_capacity(intervals.len());

        for interval in intervals {
            let end = interval[1];
            match starts.binary_search(&end) {
                Ok(position) => result.push(indexed[position].1),
                Err(position) => {
                    if position == starts.len() {
                        result.push(-1);
                    } else {
                        result.push(indexed[position].1);
                    }
                }
            }
        }

        result
    }
}
