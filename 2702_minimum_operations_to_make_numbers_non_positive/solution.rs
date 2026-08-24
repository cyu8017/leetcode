// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32, y: i32) -> i32 {
        let ok = |ops: i32| -> bool {
            let mut extra = 0i64;
            for &v in &nums {
                let remain = v as i64 - ops as i64 * y as i64;
                if remain > 0 {
                    extra += (remain + (x - y) as i64 - 1) / (x - y) as i64;
                }
            }
            extra <= ops as i64
        };
        let mut lo = 0;
        let mut hi = 0;
        for &v in &nums {
            hi = hi.max((v + y - 1) / y);
            hi = hi.max((v + x - 1) / x);
        }
        hi += nums.len() as i32;
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
