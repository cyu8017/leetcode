// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

impl Solution {
    pub fn minimum_difference(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let k = k as usize;
        (0..=nums.len() - k)
            .map(|i| nums[i + k - 1] - nums[i])
            .min()
            .unwrap()
    }
}
