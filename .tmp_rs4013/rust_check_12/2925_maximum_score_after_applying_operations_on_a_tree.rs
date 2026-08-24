struct Solution;
// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

impl Solution {
    pub fn maximum_score_after_operations(edges: Vec<Vec<i32>>, values: Vec<i32>) -> i64 {
        let n = values.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let total: i64 = values.iter().map(|&v| v as i64).sum();
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], values: &[i32]) -> i64 {
            let mut sum_kids = 0i64;
            let mut is_leaf = true;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                is_leaf = false;
                sum_kids += dfs(v, u as i32, g, values);
            }
            if is_leaf {
                return values[u] as i64;
            }
            (values[u] as i64).min(sum_kids)
        }
        total - dfs(0, -1, &g, &values)
    }
}

fn main() {}
