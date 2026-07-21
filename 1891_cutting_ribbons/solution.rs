// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

impl Solution {
    pub fn max_length(ribbons: Vec<i32>, k: i32) -> i32 {
        let can = |length: i32| -> bool {
            ribbons.iter().map(|&r| (r / length) as i64).sum::<i64>() >= k as i64
        };
        let mut lo = 1;
        let mut hi = *ribbons.iter().max().unwrap_or(&0);
        if hi == 0 {
            return 0;
        }
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        if can(lo) {
            lo
        } else {
            0
        }
    }
}
