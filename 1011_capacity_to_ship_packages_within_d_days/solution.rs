// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        let mut lo = *weights.iter().max().unwrap();
        let mut hi: i32 = weights.iter().sum();
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            let mut need = 1;
            let mut cur = 0;
            for &w in &weights {
                if cur + w > mid {
                    need += 1;
                    cur = 0;
                }
                cur += w;
            }
            if need <= days {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
