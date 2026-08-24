// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

impl Solution {
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut g = vec![0; n];
        let mut cnt = 0;
        for i in 1..n {
            if nums[i] - nums[i - 1] > max_diff {
                cnt += 1;
            }
            g[i] = cnt;
        }
        queries.iter().map(|q| g[q[0] as usize] == g[q[1] as usize]).collect()
    }
}
