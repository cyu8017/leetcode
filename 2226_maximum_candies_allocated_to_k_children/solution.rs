// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

impl Solution {
    pub fn maximum_candies(candies: Vec<i32>, k: i64) -> i32 {
        let mx = *candies.iter().max().unwrap_or(&0);
        let mut lo = 0;
        let mut hi = mx;
        let can = |mid: i32| {
            if mid == 0 {
                return true;
            }
            let mut cnt = 0i64;
            for &c in &candies {
                cnt += (c / mid) as i64;
                if cnt >= k {
                    return true;
                }
            }
            false
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
