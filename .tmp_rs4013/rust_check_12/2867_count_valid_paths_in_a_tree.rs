struct Solution;
// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

impl Solution {
    pub fn count_paths(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut is_prime = vec![true; n + 1];
        is_prime[0] = false;
        is_prime[1] = false;
        let mut i = 2;
        while i * i <= n {
            if is_prime[i] {
                let mut j = i * i;
                while j <= n {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let mut g = vec![Vec::new(); n + 1];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(u: usize, p: usize, is_prime: &[bool], g: &[Vec<usize>]) -> i32 {
            if is_prime[u] {
                return 0;
            }
            let mut sz = 1;
            for &v in &g[u] {
                if v != p {
                    sz += dfs(v, u, is_prime, g);
                }
            }
            sz
        }
        let mut ans = 0i64;
        for u in 1..=n {
            if !is_prime[u] {
                continue;
            }
            let mut total = 0i64;
            for &v in &g[u] {
                let c = dfs(v, u, &is_prime, &g) as i64;
                ans += c;
                ans += total * c;
                total += c;
            }
        }
        ans
    }
}

fn main() {}
