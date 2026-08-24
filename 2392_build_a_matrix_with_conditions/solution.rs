// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

use std::collections::VecDeque;

impl Solution {
    pub fn build_matrix(k: i32, row_conditions: Vec<Vec<i32>>, col_conditions: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let k = k as usize;
        let topo = |conds: &[Vec<i32>]| -> Option<Vec<usize>> {
            let mut g = vec![Vec::new(); k + 1];
            let mut indeg = vec![0; k + 1];
            for c in conds {
                g[c[0] as usize].push(c[1] as usize);
                indeg[c[1] as usize] += 1;
            }
            let mut q = VecDeque::new();
            for i in 1..=k {
                if indeg[i] == 0 {
                    q.push_back(i);
                }
            }
            let mut order = Vec::new();
            while let Some(u) = q.pop_front() {
                order.push(u);
                for &v in &g[u] {
                    indeg[v] -= 1;
                    if indeg[v] == 0 {
                        q.push_back(v);
                    }
                }
            }
            if order.len() != k {
                None
            } else {
                Some(order)
            }
        };
        let row_order = match topo(&row_conditions) {
            Some(o) => o,
            None => return vec![],
        };
        let col_order = match topo(&col_conditions) {
            Some(o) => o,
            None => return vec![],
        };
        let mut row_pos = vec![0; k + 1];
        let mut col_pos = vec![0; k + 1];
        for i in 0..k {
            row_pos[row_order[i]] = i;
            col_pos[col_order[i]] = i;
        }
        let mut ans = vec![vec![0; k]; k];
        for v in 1..=k {
            ans[row_pos[v]][col_pos[v]] = v as i32;
        }
        ans
    }
}
