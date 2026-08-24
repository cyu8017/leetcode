// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

use std::collections::HashMap;

impl Solution {
    pub fn subtree_inversion_sum(edges: Vec<Vec<i32>>, nums: Vec<i32>, k: i32) -> i64 {
        let n = edges.len() + 1;
        let mut graph = vec![Vec::<usize>::new(); n];
        for e in &edges {
            graph[e[0] as usize].push(e[1] as usize);
            graph[e[1] as usize].push(e[0] as usize);
        }
        let mut parent = vec![-1i32; n];
        fn dp(
            u: usize,
            steps: i32,
            inv: bool,
            k: i32,
            graph: &[Vec<usize>],
            nums: &[i32],
            parent: &mut [i32],
            memo: &mut HashMap<(usize, i32, bool), i64>,
        ) -> i64 {
            let key = (u, steps, inv);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let mut num = nums[u] as i64;
            if inv {
                num = -num;
            }
            let mut neg_num = -num;
            for &v in &graph[u] {
                if v as i32 == parent[u] {
                    continue;
                }
                parent[v] = u as i32;
                let mut ns = steps + 1;
                if ns > k {
                    ns = k;
                }
                num += dp(v, ns, inv, k, graph, nums, parent, memo);
                if steps == k {
                    neg_num += dp(v, 1, !inv, k, graph, nums, parent, memo);
                }
            }
            let mut res = num;
            if steps == k && neg_num > res {
                res = neg_num;
            }
            memo.insert(key, res);
            res
        }
        let mut memo = HashMap::new();
        dp(0, k, false, k, &graph, &nums, &mut parent, &mut memo)
    }
}
