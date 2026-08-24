#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            for j in i..n {
                let mut prev = -1;
                let mut ok = true;
                for t in 0..n {
                    if t >= i && t <= j {
                        continue;
                    }
                    if nums[t] <= prev {
                        ok = false;
                        break;
                    }
                    prev = nums[t];
                }
                if ok {
                    ans += 1;
                }
            }
        }
        ans
    }
}
