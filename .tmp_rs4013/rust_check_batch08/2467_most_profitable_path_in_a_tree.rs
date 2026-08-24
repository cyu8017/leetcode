struct Solution;
// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

impl Solution {
    pub fn most_profitable_path(edges: Vec<Vec<i32>>, bob: i32, amount: Vec<i32>) -> i32 {
        let n = amount.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut bob_time = vec![n as i32; n];
        fn find_bob(
            u: usize,
            p: i32,
            t: i32,
            g: &[Vec<usize>],
            bob_time: &mut [i32],
        ) -> bool {
            if u == 0 {
                bob_time[u] = t;
                return true;
            }
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if find_bob(v, u as i32, t + 1, g, bob_time) {
                    bob_time[u] = t;
                    return true;
                }
            }
            false
        }
        find_bob(bob as usize, -1, 0, &g, &mut bob_time);
        let mut ans = i32::MIN;
        fn dfs(
            u: usize,
            p: i32,
            t: i32,
            income: i32,
            g: &[Vec<usize>],
            amount: &[i32],
            bob_time: &[i32],
            ans: &mut i32,
        ) {
            let mut cur = amount[u];
            if t > bob_time[u] {
                cur = 0;
            } else if t == bob_time[u] {
                cur /= 2;
            }
            let income = income + cur;
            let mut is_leaf = true;
            for &v in &g[u] {
                if v as i32 != p {
                    is_leaf = false;
                    dfs(v, u as i32, t + 1, income, g, amount, bob_time, ans);
                }
            }
            if is_leaf && income > *ans {
                *ans = income;
            }
        }
        dfs(0, -1, 0, 0, &g, &amount, &bob_time, &mut ans);
        ans
    }
}

fn main() {}
