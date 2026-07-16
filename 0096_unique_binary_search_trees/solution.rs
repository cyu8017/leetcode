// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

impl Solution {
    pub fn num_trees(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        for nodes in 1..=n {
            for root in 1..=nodes {
                dp[nodes] += dp[root - 1] * dp[nodes - root];
            }
        }
        dp[n]
    }
}
