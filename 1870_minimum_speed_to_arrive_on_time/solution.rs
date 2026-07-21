// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        let n = dist.len();
        if (n as f64 - 1.0) >= hour {
            return -1;
        }
        let can_arrive = |speed: i32| -> bool {
            let mut time = 0.0f64;
            for i in 0..n - 1 {
                time += ((dist[i] + speed - 1) / speed) as f64;
            }
            time += dist[n - 1] as f64 / speed as f64;
            time <= hour
        };
        if !can_arrive(10_000_000) {
            return -1;
        }
        let mut lo = 1;
        let mut hi = 10_000_000;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if can_arrive(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
