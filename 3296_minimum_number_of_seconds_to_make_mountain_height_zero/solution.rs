// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

impl Solution {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        let ok = |t: i64| -> bool {
            let mut total = 0i64;
            for &w in &worker_times {
                let mut lo = 0i64;
                let mut hi = mountain_height as i64;
                while lo < hi {
                    let mid = (lo + hi + 1) / 2;
                    if w as i64 * mid * (mid + 1) / 2 <= t {
                        lo = mid;
                    } else {
                        hi = mid - 1;
                    }
                }
                total += lo;
                if total >= mountain_height as i64 {
                    return true;
                }
            }
            total >= mountain_height as i64
        };
        let mut lo = 0i64;
        let mut hi = 10i64.pow(18);
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
