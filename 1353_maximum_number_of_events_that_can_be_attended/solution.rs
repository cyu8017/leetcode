// LeetCode 1353 - Maximum Number of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn max_events(mut events: Vec<Vec<i32>>) -> i32 {
        events.sort_unstable();
        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut i = 0;
        let mut ans = 0;
        let mut day = 0;
        while i < events.len() || !heap.is_empty() {
            if heap.is_empty() {
                day = day.max(events[i][0]);
            }
            while i < events.len() && events[i][0] <= day {
                heap.push(Reverse(events[i][1]));
                i += 1;
            }
            while heap.peek().map(|r| r.0 < day).unwrap_or(false) {
                heap.pop();
            }
            if heap.pop().is_some() {
                ans += 1;
                day += 1;
            }
        }
        ans
    }
}
