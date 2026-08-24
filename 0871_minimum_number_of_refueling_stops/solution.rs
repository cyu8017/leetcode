// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

use std::collections::BinaryHeap;

impl Solution {
    pub fn min_refuel_stops(target: i32, start_fuel: i32, mut stations: Vec<Vec<i32>>) -> i32 {
        let mut pq = BinaryHeap::new();
        stations.push(vec![target, 0]);
        let mut ans = 0;
        let mut prev = 0;
        let mut fuel = start_fuel as i64;
        for st in stations {
            let pos = st[0];
            let gas = st[1];
            fuel -= (pos - prev) as i64;
            while !pq.is_empty() && fuel < 0 {
                fuel += pq.pop().unwrap() as i64;
                ans += 1;
            }
            if fuel < 0 {
                return -1;
            }
            pq.push(gas);
            prev = pos;
        }
        ans
    }
}
