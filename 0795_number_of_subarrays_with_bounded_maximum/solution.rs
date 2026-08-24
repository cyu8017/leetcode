// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

impl Solution {
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        Self::count_at_most(&nums, right) - Self::count_at_most(&nums, left - 1)
    }

    fn count_at_most(nums: &[i32], bound: i32) -> i32 {
        let mut ans = 0;
        let mut cur = 0;
        for &num in nums {
            if num <= bound {
                cur += 1;
                ans += cur;
            } else {
                cur = 0;
            }
        }
        ans
    }
}
