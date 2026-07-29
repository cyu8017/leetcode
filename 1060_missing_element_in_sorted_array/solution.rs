// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

impl Solution {
    pub fn missing_element(nums: Vec<i32>, k: i32) -> i32 {
        let missing = |i: usize| -> i32 { nums[i] - nums[0] - i as i32 };
        let n = nums.len();
        if k > missing(n - 1) {
            return nums[n - 1] + k - missing(n - 1);
        }
        let mut lo = 0usize;
        let mut hi = n - 1;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if missing(mid) < k {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        nums[lo - 1] + k - missing(lo - 1)
    }
}
