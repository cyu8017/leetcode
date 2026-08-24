// LeetCode 3835 - Count Subarrays With Cost Less Than or Equal to K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

use std::collections::VecDeque;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut ans = 0i64;
        let mut q1 = VecDeque::new();
        let mut q2 = VecDeque::new();
        let mut l = 0usize;
        for r in 0..nums.len() {
            let x = nums[r];
            while q1.back().map(|&i| nums[i] <= x).unwrap_or(false) {
                q1.pop_back();
            }
            while q2.back().map(|&i| nums[i] >= x).unwrap_or(false) {
                q2.pop_back();
            }
            q1.push_back(r);
            q2.push_back(r);
            while l < r
                && (nums[*q1.front().unwrap()] as i64 - nums[*q2.front().unwrap()] as i64)
                    * (r - l + 1) as i64
                    > k
            {
                l += 1;
                if *q1.front().unwrap() < l {
                    q1.pop_front();
                }
                if *q2.front().unwrap() < l {
                    q2.pop_front();
                }
            }
            ans += (r - l + 1) as i64;
        }
        ans
    }
}
