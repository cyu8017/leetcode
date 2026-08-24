// LeetCode 3824 - Minimum K to Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

impl Solution {
    pub fn minimum_k(nums: Vec<i32>) -> i32 {
        let check = |k: i32| {
            let mut t = 0i64;
            for &x in &nums {
                t += (x as i64 + k as i64 - 1) / k as i64;
            }
            t <= k as i64 * k as i64
        };
        let mut lo = 1;
        let mut hi = 100000;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
