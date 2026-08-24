struct Solution;
// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

impl Solution {
    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], values: &[i32], k: i32, ans: &mut i32) -> i32 {
            let mut sum = values[u] % k;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                sum = (sum + dfs(v, u as i32, g, values, k, ans)) % k;
            }
            if sum == 0 {
                *ans += 1;
            }
            sum
        }
        let mut ans = 0;
        dfs(0, -1, &g, &values, k, &mut ans);
        ans
    }
}

fn main() {}
