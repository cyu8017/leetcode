// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

impl Solution {
    pub fn max_value(n: i32, index: i32, max_sum: i32) -> i32 {
        fn min_side_sum(value: i64, count: i64) -> i64 {
            if value > count {
                (value - 1 + value - count) * count / 2
            } else {
                value * (value - 1) / 2 + (count - value + 1)
            }
        }

        let (n, index, max_sum) = (n as i64, index as i64, max_sum as i64);
        let mut lo = 1i64;
        let mut hi = max_sum;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            let total = min_side_sum(mid, index) + mid + min_side_sum(mid, n - index - 1);
            if total <= max_sum {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
