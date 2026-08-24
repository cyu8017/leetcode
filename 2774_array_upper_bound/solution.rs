// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

impl Solution {
    pub fn upper_bound(nums: Vec<i32>, target: i32) -> i32 {
        let mut lo = 0i32;
        let mut hi = nums.len() as i32;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if nums[mid as usize] <= target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        lo
    }
}
