// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_difference(nums: Vec<i32>) -> i64 {
        let n = nums.len() / 3;
        let mut left = vec![0i64; nums.len()];
        let mut right = vec![0i64; nums.len()];
        let mut hmax = BinaryHeap::new();
        let mut sum = 0i64;
        for i in 0..n {
            hmax.push(nums[i]);
            sum += nums[i] as i64;
        }
        left[n - 1] = sum;
        for i in n..2 * n {
            hmax.push(nums[i]);
            sum += nums[i] as i64;
            sum -= hmax.pop().unwrap() as i64;
            left[i] = sum;
        }
        let mut hmin = BinaryHeap::new();
        sum = 0;
        for i in (2 * n..nums.len()).rev() {
            hmin.push(Reverse(nums[i]));
            sum += nums[i] as i64;
        }
        right[2 * n] = sum;
        for i in (n..2 * n).rev() {
            hmin.push(Reverse(nums[i]));
            sum += nums[i] as i64;
            sum -= hmin.pop().unwrap().0 as i64;
            right[i] = sum;
        }
        let mut ans = left[n - 1] - right[n];
        for i in n..2 * n {
            ans = ans.min(left[i] - right[i + 1]);
        }
        ans
    }
}
