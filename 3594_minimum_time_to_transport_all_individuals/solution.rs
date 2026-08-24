// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

impl Solution {
    pub fn min_time(n: i32, k: i32, m: i32, mut time: Vec<i32>, mul: Vec<f64>) -> f64 {
        time.sort();
        let mut total = 0.0;
        let mut stage = 0usize;
        let mut left = n;
        let m = m as usize;
        while left > 0 {
            let take = k.min(left);
            let slow = time[(left - 1) as usize];
            total += slow as f64 * mul[stage % m];
            left -= take;
            stage += 1;
            if left > 0 {
                total += time[0] as f64 * mul[stage % m];
                stage += 1;
            }
        }
        total
    }
}
