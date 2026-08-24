// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

use std::collections::HashSet;

impl Solution {
    pub fn centered_subarrays(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut st = HashSet::new();
            let mut s = 0;
            for j in i..n {
                s += nums[j];
                st.insert(nums[j]);
                if st.contains(&s) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
