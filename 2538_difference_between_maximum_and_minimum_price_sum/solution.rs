// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

impl Solution {
    pub fn max_output(n: i32, edges: Vec<Vec<i32>>, price: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0i64;
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], price: &[i32], ans: &mut i64) -> i64 {
            let mut max_child = 0i64;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let child = dfs(v, u as i32, g, price, ans);
                if child > max_child {
                    max_child = child;
                }
                if child > *ans {
                    *ans = child;
                }
            }
            price[u] as i64 + max_child
        }
        dfs(0, -1, &g, &price, &mut ans);
        ans
    }
}
