struct Solution;
// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

impl Solution {
    pub fn max_star_sum(vals: Vec<i32>, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = vals.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut ans = vals[0];
        for i in 0..n {
            let mut neigh = Vec::new();
            for &v in &g[i] {
                if vals[v] > 0 {
                    neigh.push(vals[v]);
                }
            }
            neigh.sort_unstable_by(|a, b| b.cmp(a));
            let mut sum = vals[i];
            for j in 0..neigh.len().min(k as usize) {
                sum += neigh[j];
            }
            if sum > ans {
                ans = sum;
            }
        }
        ans
    }
}

fn main() {}
