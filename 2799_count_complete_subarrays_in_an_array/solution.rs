// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

use std::collections::HashSet;

impl Solution {
    pub fn count_complete_subarrays(nums: Vec<i32>) -> i32 {
        let need = nums.iter().copied().collect::<HashSet<_>>().len();
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut seen = HashSet::new();
            for j in i..n {
                seen.insert(nums[j]);
                if seen.len() == need {
                    ans += (n - j) as i32;
                    break;
                }
            }
        }
        ans
    }
}
