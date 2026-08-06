// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

impl Solution {
    pub fn kth_smallest_subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        fn count(nums: &[i32], limit: i32) -> i32 {
            let mut total = 0;
            let mut left = 0;
            let mut ans = 0;
            for (right, &value) in nums.iter().enumerate() {
                total += value;
                while total > limit {
                    total -= nums[left];
                    left += 1;
                }
                ans += (right - left + 1) as i32;
            }
            ans
        }

        let mut lo = *nums.iter().min().unwrap();
        let mut hi: i32 = nums.iter().sum();
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if count(&nums, mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
