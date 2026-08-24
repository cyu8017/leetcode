// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

impl Solution {
    pub fn minimum_time(d: Vec<i32>, r: Vec<i32>) -> i64 {
        let ok = |t: i64| -> bool {
            let w0 = t - t / r[0] as i64;
            let w1 = t - t / r[1] as i64;
            w0 + w1 >= d[0] as i64 + d[1] as i64
        };
        let mut lo = 1i64;
        let mut hi = 8_000_000_000_000_000_000i64;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
