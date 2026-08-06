// LeetCode 1482 - Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

impl Solution {
    pub fn min_days(bloom_day: Vec<i32>, m: i32, k: i32) -> i32 {
        if m as i64 * k as i64 > bloom_day.len() as i64 {
            return -1;
        }
        let possible = |day: i32| -> bool {
            let mut bouquets = 0;
            let mut run = 0;
            for &x in &bloom_day {
                if x <= day {
                    run += 1;
                    if run == k {
                        bouquets += 1;
                        run = 0;
                    }
                } else {
                    run = 0;
                }
            }
            bouquets >= m
        };
        let mut lo = *bloom_day.iter().min().unwrap();
        let mut hi = *bloom_day.iter().max().unwrap();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if possible(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
