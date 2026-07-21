// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        (0..n / 2)
            .map(|i| nums[i] + nums[n - 1 - i])
            .max()
            .unwrap_or(0)
    }
}
