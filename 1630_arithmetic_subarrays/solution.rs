// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

impl Solution {
    pub fn check_arithmetic_subarrays(nums: Vec<i32>, l: Vec<i32>, r: Vec<i32>) -> Vec<bool> {
        l.into_iter()
            .zip(r)
            .map(|(a, b)| {
                let mut x = nums[a as usize..=b as usize].to_vec();
                x.sort_unstable();
                if x.len() < 3 {
                    return true;
                }
                let diff = x[1] - x[0];
                x.windows(2).all(|w| w[1] - w[0] == diff)
            })
            .collect()
    }
}
