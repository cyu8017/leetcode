// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

impl Solution {
    pub fn answer_queries(mut nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        for i in 1..nums.len() {
            nums[i] += nums[i - 1];
        }
        queries
            .into_iter()
            .map(|q| nums.partition_point(|&x| x <= q) as i32)
            .collect()
    }
}
