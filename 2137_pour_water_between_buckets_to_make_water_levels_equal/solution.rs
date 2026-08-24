// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

impl Solution {
    pub fn equalize_water(buckets: Vec<i32>, loss: i32) -> f64 {
        let mut lo = 0.0;
        let mut hi = *buckets.iter().max().unwrap_or(&0) as f64;
        let can = |x: f64| {
            let mut have = 0.0;
            let mut need = 0.0;
            for &b in &buckets {
                let b = b as f64;
                if b >= x {
                    have += b - x;
                } else {
                    need += x - b;
                }
            }
            have * (1.0 - loss as f64 / 100.0) >= need
        };
        for _ in 0..60 {
            let mid = (lo + hi) / 2.0;
            if can(mid) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        lo
    }
}
