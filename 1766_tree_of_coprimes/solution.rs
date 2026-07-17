// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

impl Solution {
    pub fn get_coprimes(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> Vec<i32> {
        fn gcd(a: i32, b: i32) -> i32 {
            if b == 0 { a } else { gcd(b, a % b) }
        }

        fn dfs(
            node: usize,
            parent: i32,
            depth: i32,
            nums: &[i32],
            adj: &[Vec<usize>],
            path: &mut Vec<Vec<(i32, i32)>>,
            ans: &mut Vec<i32>,
        ) {
            let mut best = (-1, -1);
            let val = nums[node];
            for d in 1..=50 {
                if gcd(val, d) == 1 && !path[d as usize].is_empty() {
                    let cand = *path[d as usize].last().unwrap();
                    if cand.0 > best.0 {
                        best = cand;
                    }
                }
            }
            ans[node] = best.1;
            path[val as usize].push((depth, node as i32));
            for &nxt in &adj[node] {
                if nxt as i32 != parent {
                    dfs(nxt, node as i32, depth + 1, nums, adj, path, ans);
                }
            }
            path[val as usize].pop();
        }

        let n = nums.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut ans = vec![-1; n];
        let mut path: Vec<Vec<(i32, i32)>> = vec![Vec::new(); 51];
        dfs(0, -1, 0, &nums, &adj, &mut path, &mut ans);
        ans
    }
}
