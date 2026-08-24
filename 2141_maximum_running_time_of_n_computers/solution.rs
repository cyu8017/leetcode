// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

impl Solution {
    pub fn max_run_time(n: i32, batteries: Vec<i32>) -> i64 {
        let sum: i64 = batteries.iter().map(|&b| b as i64).sum();
        let n = n as i64;
        let mut lo = 1i64;
        let mut hi = sum / n;
        let can = |t: i64| {
            let mut need = 0i64;
            for &b in &batteries {
                need += (b as i64).min(t);
            }
            need >= t * n
        };
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
