// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

impl Solution {
    pub fn minmax_gas_dist(stations: Vec<i32>, k: i32) -> f64 {
        let can = |dist: f64| -> bool {
            let mut needed = 0;
            for i in 1..stations.len() {
                needed += ((stations[i] - stations[i - 1]) as f64 / dist) as i32;
            }
            needed <= k
        };
        let mut lo = 0.0;
        let mut hi = (stations[stations.len() - 1] - stations[0]) as f64;
        while hi - lo > 1e-6 {
            let mid = (lo + hi) / 2.0;
            if can(mid) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        hi
    }
}
