// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

use std::collections::HashSet;

impl Solution {
    pub fn latest_time_catch_the_bus(mut buses: Vec<i32>, mut passengers: Vec<i32>, capacity: i32) -> i32 {
        buses.sort_unstable();
        passengers.sort_unstable();
        let mut pos = 0usize;
        for bi in 0..buses.len() {
            let bus = buses[bi];
            let mut cap = capacity;
            while cap > 0 && pos < passengers.len() && passengers[pos] <= bus {
                pos += 1;
                cap -= 1;
            }
            if bi == buses.len() - 1 {
                let mut cand = if cap == 0 { passengers[pos - 1] } else { bus };
                let taken: HashSet<i32> = passengers.iter().copied().collect();
                while taken.contains(&cand) {
                    cand -= 1;
                }
                return cand;
            }
        }
        -1
    }
}
