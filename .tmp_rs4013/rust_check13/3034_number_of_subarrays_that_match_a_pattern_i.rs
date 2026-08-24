#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

impl Solution {
    pub fn count_matching_subarrays(nums: Vec<i32>, pattern: Vec<i32>) -> i32 {
        let f = |a: i32, b: i32| -> i32 {
            if a == b {
                0
            } else if a < b {
                1
            } else {
                -1
            }
        };
        let n = nums.len();
        let m = pattern.len();
        let mut ans = 0;
        for i in 0..n.saturating_sub(m) {
            let mut ok = 1;
            for k in 0..m {
                if f(nums[i + k], nums[i + k + 1]) != pattern[k] {
                    ok = 0;
                    break;
                }
            }
            ans += ok;
        }
        ans
    }
}
