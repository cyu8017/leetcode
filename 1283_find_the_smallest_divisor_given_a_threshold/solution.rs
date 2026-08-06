// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

impl Solution {
    pub fn smallest_divisor(nums: Vec<i32>, threshold: i32) -> i32 {
        let mut lo = 1;
        let mut hi = *nums.iter().max().unwrap();
        while lo < hi {
            let mid = (lo + hi) / 2;
            let sum: i32 = nums.iter().map(|&x| (x + mid - 1) / mid).sum();
            if sum <= threshold {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
