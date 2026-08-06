// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

impl Solution {
    pub fn minimum_perimeter(needed_apples: i64) -> i64 {
        let mut lo: i64 = 1;
        let mut hi: i64 = 100_000;
        while lo < hi {
            let mid = (lo + hi) / 2;
            let apples = 2 * mid * (mid + 1) * (2 * mid + 1);
            if apples >= needed_apples {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        8 * lo
    }
}
