// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_interval(mut intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        intervals.sort_by_key(|iv| iv[0]);
        let mut indexed: Vec<(usize, i32)> = queries.iter().copied().enumerate().collect();
        indexed.sort_by_key(|&(_, q)| q);

        let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        let mut answer = vec![-1; queries.len()];
        let mut interval_idx = 0usize;

        for (query_idx, query) in indexed {
            while interval_idx < intervals.len() && intervals[interval_idx][0] <= query {
                let left = intervals[interval_idx][0];
                let right = intervals[interval_idx][1];
                heap.push(Reverse((right - left + 1, right)));
                interval_idx += 1;
            }
            while let Some(Reverse((_, right))) = heap.peek() {
                if *right < query {
                    heap.pop();
                } else {
                    break;
                }
            }
            if let Some(Reverse((size, _))) = heap.peek() {
                answer[query_idx] = *size;
            }
        }
        answer
    }
}
