// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        let mn = *time.iter().min().unwrap() as i64;
        let mut lo = 1i64;
        let mut hi = mn * total_trips as i64;
        let can = |mid: i64| {
            let mut trips = 0i64;
            for &t in &time {
                trips += mid / t as i64;
                if trips >= total_trips as i64 {
                    return true;
                }
            }
            false
        };
        while lo < hi {
            let mid = (lo + hi) / 2;
            if can(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
